from django.http import HttpResponse

def hello(request):
    return HttpResponse('<a href="blog/"><h1>heading</h1></a>')