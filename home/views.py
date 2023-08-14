from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import stats, course, coursePage, catagory, alumni, member, events, clubs, developingProgram, curiousProgram, schedule, startProgram, ventureProgram, competition, about, previousSpeaker, launch, NotionLink, FairParticipant, FairYear, JobFair
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from datetime import date
from django.http import Http404

# Create your views here.

programCatagories = [
        {"name": "Get Curious", "img": "/media/img/curious.jpg", "tags": ["Investor", "Joiner"], "link": "/get-curious"},
        {"name": "Getting Started", "img":"/media/img/started.jpg", "tags": ["Founder"],  "link": "/started"},
        {"name": "Developing Your Idea", "img":"/media/img/idea.jpg", "tags": ["Founder"], "link": "/developing"},
        {"name": "Accelerate Your Venture", "img":"/media/img/accelerate.jpg", "tags": ["Founder", "Investor"], "link": "/venture"},
        {"name": "Competitions", "img":"/media/img/competition.jpg", "tags": ["Joiner", "Investor", "Founder"], "link": "/competitions"},
        {"name": "Speaker Series", "img":"/media/img/speaker.jpg", "tags": ["Joiner", "Investor", "Founder"], "link": "/speaker"},
        {"name": "Student Clubs", "img":"/media/img/clubs.jpg", "tags": ["Joiner", "Investor"], "link": "/clubs"},
    ]


def getNotion():
    link = ""
    if(len(NotionLink.objects.all()) > 0):
        link = NotionLink.objects.all()[0]
        return link.link
    else:
        return ""

def index(request):

    return render(request, "home/index.html", {
        "stats": stats.objects.all(),
        "alumni": alumni.objects.all(),
        "programs": programCatagories,
        "notion": getNotion(),
    })

def programs(request):
    return render(request, "home/programs.html", {
        "programs": programCatagories,
        "notion": getNotion(),
    })

def courses(request, type):
    for page in coursePage.objects.all():
        if page.kind.lower() == type.lower():
            return render(request, "home/courses.html", {
                "page": page
                })

def plan(request, type):
    if request.method == "GET":
        if type != "undergraduate" and type != "graduate":
            raise Http404
        for page in coursePage.objects.all():
            if page.kind.lower() == type.lower():
                return render(request, "home/plan.html",{
                    "page":page,
                    "options": catagory.objects.all(),
                    "notion": getNotion(),

                })

@csrf_exempt
def getPlan(request):
    if request.method == "POST":
        data = json.loads(request.body)
        selected = data.get("selected")
        kind = data.get("kind")

        selectedObjects = []
        for s in selected:
            selectedObjects.append(catagory.objects.get(catagory=s))
        

        for page in coursePage.objects.all():
            if page.kind.lower() == kind.lower():
                courses = []
                for c in page.courses.all():
                    for objects in selectedObjects:
                        add = {"course":c.course, "offeredIn":c.offeredIn, "description":c.description, "requiredForMinor": c.requiredForMinor,
                        "capstone": c.capstone}
                        if objects in c.catagories.all() and add not in courses:
                            courses.append(add)

                eventsList = []
                for event in events.objects.all():
                    for objects in selectedObjects:
                        add = {"event":event.event, "description":event.description, "image":str(event.image),
                        "location":event.location, "date": event.date, "start": event.start, "end": event.end}
                        if objects in event.catagories.all() and add not in eventsList:
                            eventsList.append(add)

                programList = []
                for program in programCatagories:
                    for objects in selectedObjects:
                        
                        if objects.catagory in program["tags"] and program not in programList:
                            programList.append(program)
    
                return JsonResponse({"courses": courses, "events": eventsList, "programs": programList}, safe=False)

@csrf_exempt
def getEvents(request):
    if request.method == "POST":
        data = json.loads(request.body)
        selected = data.get("selected")

        selectedObjects = []
        for s in selected:
            selectedObjects.append(catagory.objects.get(catagory=s))
        
        eventsList = []
        for event in events.objects.all():
            for objects in selectedObjects:
                add = {"event":event.event, "description":event.description, "image":str(event.image),
                "location":event.location}
                if objects in event.catagories.all() and add not in eventsList:
                    eventsList.append(add)

        return JsonResponse(eventsList, safe=False)


def idea(request):
    
    upcoming = []
    for event in events.objects.all():
        if event.date >= date.today():
            upcoming.append(event)

    catagories = []

    for c in programCatagories:
        if "Founder" in c["tags"]:
            catagories.append(c)

    return render(request, "home/idea.html", {
            "members": member.objects.all(),
            "events": upcoming,
            "programs": catagories ,
            "notion": getNotion(),

    })

def club(request):
    return render(request, "home/clubs.html", {
        "clubs": clubs.objects.all(),
        "notion": getNotion(),
    })  

def developing(request):
    return render(request, "home/developing.html", {
        "programs": developingProgram.objects.all(),
        "notion": getNotion(),
    })

def developingPage(request,program):
    try:
        pro = developingProgram.objects.get(program=program)
    except developingProgram.DoesNotExist:
        raise Http404

    return render(request, "home/developingPage.html", {
        "program": pro,
        "notion": getNotion(),
    })

def curious(request):
    if len(JobFair.objects.all()) > 0:
        fair = JobFair.objects.all()[0]
    else:
        fair = {}

    return render(request, "home/curious.html",{
        "programs": curiousProgram.objects.all(),
        "fair": fair,
        "notion": getNotion(),
    })

def curiousPage(request, program):
   
    try:
        pro = curiousProgram.objects.get(program=program)
    except curiousProgram.DoesNotExist:
        raise Http404
    
    return render(request, "home/curiousPage.html", {
        "program": pro,
        "notion": getNotion(),
    })

def started(request):
    return render(request, "home/started.html",{
        "programs": startProgram.objects.all(),
        "notion": getNotion(),
    })

def venture(request):
    return render(request, "home/venture.html", {
        "programs": ventureProgram.objects.all(),
        "notion": getNotion(),
    })
def venturePage(request, program):
    try:
        pro = ventureProgram.objects.get(program=program)
    except ventureProgram.DoesNotExist:
        raise Http404

    return render(request, "home/venturePage.html", {
        "program": pro,
        "notion": getNotion(),
    })

def competitions(request):
    return render(request, "home/competitions.html",{
        "programs": competition.objects.all(),
        "notion": getNotion(),
    })

def competitionPage(request, program):
    try:
        pro = competition.objects.get(program=program)
    except competition.DoesNotExist:
        raise Http404
    return render(request, "home/competitionPage.html", {
        "program": pro,
        "notion": getNotion(),
    })

def speaker(request):
    return render(request, "home/speaker.html", {
        "programs": competition.objects.all(),
        "notion": getNotion(),
    })

def aboutPage(request):
    if len(about.objects.all()) > 0:
        res = about.objects.all()[0]
    else:
        res = {}
    return render(request, "home/about.html", {
        "about": res,
        "notion": getNotion(),
    })

def team(request):
    return render(request, "home/team.html", {
        "members": member.objects.filter(isFaculty=True),
        "notion": getNotion(),
    })

def advisor(request):
    return render(request, "home/advisors.html", {
      "members": member.objects.filter(isFaculty=False),
      "notion": getNotion(),
    })

def memberPage(request,name):

    try:
        print(name)
        res = member.objects.get(name=name)
    except member.DoesNotExist:
        raise Http404

    return render(request, "home/member.html", {
        "member": res,
        "notion": getNotion(),
    })

def minor(request):
    page = coursePage.objects.get(kind="Undergraduate")

    return render(request, "home/courses.html", {
        "page": page,
        "required": course.objects.filter(requiredForMinor=True),
        "capstone": course.objects.filter(capstone=True),
        "notion": getNotion(),
    })

def speakers(request):
    return render(request, "home/speaker.html", {
        "previousSpeakers": previousSpeaker.objects.all(),
        "launch": launch.objects.all(),
        "notion": getNotion(),
    })

def location(request):
    print("hi")
    return render(request, "home/location.html", {
        "notion": getNotion(),
    })

def JobFairPage(request, fair):
    print("hi")
    try:
        program = JobFair.objects.get(program=fair)
    except JobFair.DoesNotExist:
        raise Http404

    return render(request, "home/jobFair.html", {
        "notion": getNotion(),
        "program": program,
    })

