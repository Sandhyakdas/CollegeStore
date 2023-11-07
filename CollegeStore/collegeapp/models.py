from django.db import models

# Create your models here.
class course(models.Model):
    #objects = None
    #objects = None
    objects = None
    coursename=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="gallary")
def __str__(self):
        return self.name