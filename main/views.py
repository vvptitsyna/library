from django.shortcuts import render


def homeindex(request):
    return render(request, 'main/main.html')
# Create your views here.
