from django.http import HttpResponse
def show_text(request):
    resp="<h2>welcome to the django course!!!</h2>"
    return HttpResponse(resp)