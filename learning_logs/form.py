from django import forms  # import form module from django

from .models import Topic,Entry   # import the particular model you want to work with, Topic in this case


class TopicForm(forms.ModelForm):       # Define a class called TopicForm, which inherits from .ModelForm
    class Meta:                     # simplest version of a ModelForm consists of a nested Meta class
        model = Topic               # tells Django which model to base the form and which fields to include in the form.
        fields = ['text']           # build a form from the topic model and include only the text field
        labels = {'text': ''}       # tells Django not to generate a label for the text field


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}   # label is used to change the display name of the field. label accepts as input a
        # string which is element of the field.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


