from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/pages/about.html')


def exhibitions(request):
    return render(request, 'main/pages/exhibitions.html')


def blog(request):
    return render(request, 'main/pages/blog.html')


def contact(request):
    return render(request, 'main/pages/contact.html')