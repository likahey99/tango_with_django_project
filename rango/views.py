from django.shortcuts import render

from django.http import HttpResponse

def index(request):
<<<<<<< HEAD

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
=======
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. Go to <a href='/rango/'>Index</a>")
>>>>>>> dd0868081831c03af2305318197fe6aaa6af62a7

