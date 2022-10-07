from email.policy import default
from django.db import models
from django.utils import timezone





class UserDevice(models.Model):
    ip = models.CharField(max_length=250)
    device_type = models.CharField(max_length=250)
    browser_type = models.CharField(max_length=250)
    browser_version = models.CharField(max_length=250)
    os_type = models.CharField(max_length=250)
    os_version = models.CharField(max_length=250)

    def __str__(self):
        return str(self.ip) + " :::: " + str(self.device_type)+ " :::: " + str(self.browser_type)+ " :::: " + str(self.browser_version)



class Search(models.Model):
    user_device = models.ForeignKey(UserDevice, on_delete = models.CASCADE, null=True)
    movie_name = models.CharField(max_length=250)
    was_downloaded =  models.BooleanField(default = False)
    search_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user_device) + " :::: " + str(self.movie_name)+ " :::: " + str(self.search_date)




class Downloaded(models.Model):
    user_device = models.ForeignKey(UserDevice, on_delete = models.CASCADE, null=True)
    movie_name = models.CharField(max_length=250)
    downloade_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.user_device) + " :::: " + str(self.movie_name)+ " :::: " + str(self.downloade_date)

