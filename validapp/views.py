from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_text(request):
    resp="<h2>welcome to the django course!!!</h2>"
    return HttpResponse(resp)

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Jobsearch
# Create your views here.
def job(request,action):
    if action =="add":
        jb =Jobsearch(name="a.bhasha",role="frontend developer",location="banglore",salary="90000",notice_period="15",age=22)
        jb.full_clean()
        jb.save()
        return HttpResponse(f"Job is added:{jb}")
    elif action =="get":
        template_name='job_search.html'
        job_list=Jobsearch.objects.all()
        print(f"job_list:{job_list}")
        context ={"job_list":job_list }
        return render(request,template_name,context=context)


    else:
        return HttpResponse("invalid action.",status=400)


def get_job(request,id):
       template_name="job_get.html"
       jb=Jobsearch.objects.get(id=id)
       context={'jb': jb}
       return render(request,template_name,context=context)


"""def del_job(request,id):
    jb_inst=Jobsearch.objects.get(pk=id)
    jb_inst.delete()
    return redirect('jobsearch',action='get')"""


"""def upd_movie(request, id):
    mv_inst=Movie.objects.get(pk=id)
    mv_inst.title="new title"
    mv_inst.director="new director"
    mv_inst.save()
    return redirect('movie',action='get')"""