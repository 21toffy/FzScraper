from django.urls import path

from . import views

app_name='scraper'

urlpatterns = [
    path('', views.home, name='index'),
    path('generate/', views.generate_download_link, name='generate'),
    path('about/', views.about, name = 'about'),
]

