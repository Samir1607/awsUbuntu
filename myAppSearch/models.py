from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    standards = models.CharField(max_length=15, choices=(('11 th', '11 th standard'), ("12 th", "12 th standard")))
    # slug = models.SlugField(unique=False)

    def __str__(self):
        return self.name


class SamUploads(models.Model):
    name = models.CharField(max_length=200, unique=True)
    file = models.FileField(upload_to="uploads")

    def __str__(self):
        return self.name + " " + str(self.file.size)
