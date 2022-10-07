from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(UserDevice)
admin.site.register(Search)
admin.site.register(Downloaded)
