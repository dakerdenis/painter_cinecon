from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about-me/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('work/<int:pk>/', views.painting_detail, name='painting_detail'),
    path('exhibitions/', views.exhibitions, name='exhibitions'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]