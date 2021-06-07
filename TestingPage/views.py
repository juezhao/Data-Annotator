from django.shortcuts import render

def TestingPage(request):
    return render(request, 'TestingPage.html', {})