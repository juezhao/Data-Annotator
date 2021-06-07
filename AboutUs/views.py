from django.shortcuts import render

def AboutUs(request):
    return render(request, 'AboutUs.html', {})