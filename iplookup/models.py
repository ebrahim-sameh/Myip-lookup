from django.db import models

# Create your models here.
class topic(models.Model):
    ipo=models.TextField(max_length=200)
    def __str__(self):
        return self.ip