from django.urls import path

from . import views

app_name='scraper'

urlpatterns = [
    path('', views.home, name='index'),
    path('generate/', views.generate_download_link, name='generate'),
    path('paginated/', views.next_or_previous, name='paginated'),
    path('about/', views.about, name = 'about'),
]

