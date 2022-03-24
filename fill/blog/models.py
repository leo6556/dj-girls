from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now())
    published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published = timezone.now()
        self.save()

class liki(models.Model):

    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name