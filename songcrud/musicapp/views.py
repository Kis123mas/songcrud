from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, kismas this is my first web musicapp.</h1>")