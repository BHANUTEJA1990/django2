from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Int_Char
# Create your views here.
def int_char(request,action):
    if action =="add":
        ic =Int_Char(even="2",gmail="vishwateja2012@gmail.com")
        ic.full_clean()
        ic.save()
        return HttpResponse(f"INT CHAR is added:{ic}")
    elif action =="get":
        data_list=Int_Char.objects.all()
        print(f"data_list:{data_list}")
        context ={"data_list":data_list}
        return render(request,context=context)


    else:
        return HttpResponse("invalid action.",status=400)