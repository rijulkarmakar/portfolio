from django.db import models

class Blog(models.Model):
    blogNo=models.IntegerField()
    title = models.CharField(max_length=20)
    publicationDate=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField()
