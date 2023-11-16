from django.shortcuts import render

# Create your views here.
def myApp(request):
    return render(request,("index.html")),
    # return render(request,("Hello WOrld")),