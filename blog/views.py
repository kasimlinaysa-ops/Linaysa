from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Linaysa! Welcome to my Django website.")
