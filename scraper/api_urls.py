from django.urls import path

from . import api_views

app_name='scraper_api'

urlpatterns = [
    path('api_find/', api_views.home, name='index'),
    path('api_generate/', api_views.generate_download_link, name='generate'),
]

