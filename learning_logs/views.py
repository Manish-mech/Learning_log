from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, Http404

from .models import Topic, Entry
from .form import TopicForm, EntryForm


# from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def practice(request):
    return render(request, 'practice.html')


@login_required()
def topics(request):
    """Show all topics."""
    tyopics = Topic.objects.filter(owner=request.user).order_by('date_added')

    context = {'topics': tyopics}
    return render(request, 'topics.html', context)


@login_required()
def topic(request, topic_id):
    """Show a single and all its entries."""
    top = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if top.owner != request.user:
        raise Http404
    entries = top.entry_set.order_by('-date_added')
    context = {'topic': top, 'entries': entries}
    return render(request, 'topic.html', context)


@login_required()
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'new_topic.html', context)


@login_required()
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


# For editing entry
@login_required()
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)
