from django.urls import path, re_path
from learning_logs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.index, name='index'),
    # Show all topics
    path('topics', views.topics, name='topics'),
    # path('topic/<int: pk>', views.topic, name='topic'),
    # Page for all the topic
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    re_path(r'^topics/(?P<topic_id>\d+)/topics', views.topics, name='topics'),
    # Page for adding new topic
    path('new_topic', views.new_topic, name='new_topic'),
    # Page for making new entry
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Page for editing an entry
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

