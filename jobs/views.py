from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    job_obj=Job.objects  #this gets all db objects into  as python objects

    return render(request,'jobs/home.html',{'job_obj':job_obj})
