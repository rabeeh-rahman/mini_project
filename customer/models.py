from django.db import models
import datetime
import os

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/', filename)

class new_user(models.Model):
    username=models.CharField(max_length=100, null=False)
    password=models.CharField(max_length=10, null=False)
    email=models.CharField(max_length=100, null=False)

class product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    company_name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    black = models.BooleanField(default=False, help_text="0=default, 1=Black")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



