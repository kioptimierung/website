from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def agb(request):
    return render(request, 'agb.html')

def datenschutz(request):
    return render(request, 'datenschutz.html')

def impressum(request):
    return render(request, 'impressum.html')

def services(request):
    return render(request, 'services.html')

def service_details(request):
    return render(request, 'services-details.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'prices.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'blog-details.html')

def contact(request):
    return render(request, 'contact.html')

def page_not_found(request):
    return render(request, '404.html')
