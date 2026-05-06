from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about-me/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('exhibitions/', views.exhibitions, name='exhibitions'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]