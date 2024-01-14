# == This code was created by https://noauto-nolife.com/post/django-auto-create-views/ == #

from django.shortcuts import render,redirect
from django.views import View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Topic
from .forms import TopicForm

class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        context["topics"] = Topic.objects.all()

        return render(request, "bbs/index.html", context)

    def post(self, request, *args, **kwargs):

        data    = { "error": True }
        form    = TopicForm(request.POST)

        if form.is_valid():
            print("保存")
            form.save()
        else:
            print(form.errors)


        context = {}
        context["topics"]   = Topic.objects.all()

        data["content"]     = render_to_string("bbs/content.html", context, request)
        data["error"]       = False

        return JsonResponse(data)

index   = IndexView.as_view()

class TopicUpdateView(View):
    def post(self, request, pk, *args, **kwargs):

        topic = Topic.objects.filter(id=pk).first()
        form = TopicForm(request.POST, instance=topic)

        if form.is_valid():
            print("編集")
            form.save()
        else:
            print(form.errors)

        return redirect("bbs:topic_update")

topic_update   = TopicUpdateView.as_view()

class TopicDeleteView(View):
    def post(self, request, pk, *args, **kwargs):

        topic = Topic.objects.filter(id=pk).first()
        topic.delete()

        return redirect("bbs:topic_delete")

topic_delete   = TopicDeleteView.as_view()




"""
from django.shortcuts import render
from django.views import View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Topic
from .forms import TopicForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        json    = { "error":True }
        form    = TopicForm(request.POST)

        print(request.POST)

        if not form.is_valid():
            print("Validation Error")
            print(form.errors)
            return JsonResponse(json)

        form.save()
        json["error"]   = False

        topics          = Topic.objects.all()
        context         = { "topics":topics }
        content         = render_to_string("bbs/content.html",context,request)

        json["content"] = content

        return JsonResponse(json)

index   = IndexView.as_view()

"""
