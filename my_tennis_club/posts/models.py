# c:\mytennis_club\my_tennis_club\posts

from django.db import models

# Create your models here.
class Post(models.Model):  # new
    text = models.TextField()

    def __str__(self):  # new
        #return self.text[:50]
        return f"{self.id} {self.text}"

