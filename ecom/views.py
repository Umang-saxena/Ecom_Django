from django.http import HttpResponse



def index(request):
    return HttpResponse("Home Page Of Admin")