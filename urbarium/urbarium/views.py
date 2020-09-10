from django.shortcuts import render


def home(request):
    return render(request, 'urbarium/homepage.html')

def about(request):
    return render(request, 'urbarium/about.html')
