# from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    return HttpResponse("Test URL")


# newPerson, all, update, moreThan21

def newPerson(request):
    newObject = Person(name = "Kevin", age=22, birthday = "1996-01-01")
    newObject.save()
    return HttpResponse(newObject)

def all(request):
    allNames = ""
    allEntries = Person.objects.all()

    for eachElement in allEntries:
        allNames+= eachElement.name + "<br>"

    return HttpResponse(allNames)


def moreThan21(request):
    onlyObjectsGreaterThan21 = Person.objects.filter(age__gt = 21)
    return HttpResponse(onlyObjectsGreaterThan21)

def update(request):
    updateErin = Person.objects.filter(age__gt = 21)
    updateErin = updateErin[0]
    updateErin[0].name = "Kevin"
    updateErin[0].save()
    return HttpResponse(updateErin[0])