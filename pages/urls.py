from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agb/', views.agb, name='agb'),
    path('impressum/', views.impressum, name='impressum'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),

    path('services/', views.services, name='services'),
    path('service_details/', views.service_details, name='service_details'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    # Add a catch-all 404 page
    #path('404/', views.page_not_found, name='page_not_found'),
]
