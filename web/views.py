from django.shortcuts import render

def home(request):
    return render(request, 'web/index.html')

def about(request):
    return render(request, 'web/about.html')

def portfolio(request):
    return render(request, 'web/portfolio.html')

def contact(request):
    return render(request, 'web/contacto.html')
