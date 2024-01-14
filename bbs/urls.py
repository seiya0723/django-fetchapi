# == This code was created by https://noauto-nolife.com/post/django-auto-create-urls/ == #

from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [
    path("", views.index, name="index"),
    path("topic_update/<int:pk>/", views.topic_update, name="topic_update"),
    path("topic_delete/<int:pk>/", views.topic_delete, name="topic_delete"),
]
