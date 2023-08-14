from django.shortcuts import render
from django.urls import path
from django.urls import re_path

# Create your views here.

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/<str:type>", views.courses, name="courses"),
    path("plan/<str:type>", views.plan, name="plan"),
    path("getPlan/", views.getPlan),
    path("idea", views.idea, name="idea"),
    path("clubs", views.club,),
    path("developing", views.developing),
    path("get-curious", views.curious),
    path("started", views.started),
    path("venture", views.venture),
    path("competitions", views.competitions),
    path("about", views.aboutPage),
    path("team", views.team),
    path("advisor", views.advisor),
    path("member/<str:name>", views.memberPage),
    path("minor", views.minor),
    path("speaker", views.speakers),
    path("location", views.location),
    path("developing/<str:program>", views.developingPage),
    path("curious/<str:program>", views.curiousPage),
    path("venture/<str:program>", views.venturePage),
    path("competition/<str:program>", views.competitionPage),
    path("programs", views.programs),
    path("jobfair/<str:fair>", views.JobFairPage),


]