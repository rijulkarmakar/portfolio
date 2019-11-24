from django.db import models

class Blog(models.Model):
    blogNo=models.IntegerField()
    title = models.CharField(max_length=20)
    publicationDate=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub_Date(self):
        return self.publicationDate.strftime('%b %d %Y')
