from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    profile = Profile.objects.all()
    project = Project.objects.all().order_by('-date')
    experience = Experience.objects.all().order_by('-date')
    skill = Skill.objects.all()
    header = Header.objects.all()
    footer = Footer.objects.all()
    publication = Publication.objects.all().order_by('-date')
    certification = Certification.objects.all().order_by('-date')
    education = Education.objects.all().order_by('-date')
    award = Award.objects.all().order_by('-date')
    context = {
        'project':project,
        'profile':profile,
        'experience':experience,
        'skill':skill,
        'header':header,
        'footer':footer,
        'publication':publication,
        'certification':certification,
        'education':education,
        'award':award
    }
    return render (request,'main.html',context)