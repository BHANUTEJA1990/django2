from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Media


def show_media(request):
    resp="<h2>welcome to the page for media in django course!!!</h2>"
    return HttpResponse(resp)

def media(request,action):
    if action =="add":
        md =Media(name="pic1",type="image",format="jpg",size="10",duration_secs="0")
        md.save()
        return HttpResponse(f"Movies is added:{md}")
    elif action =="get":
        template_name='media_demo.html'
        media_list=Media.objects.all()
      #  print(f"media_list:{media_list}")
        context ={"media_list":media_list}
        return render(request,template_name,context=context)
    else:
        return HttpResponse("invalid action.",status=400)