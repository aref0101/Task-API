from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()
from django.conf import settings

# Create your models here.

class Task(models.Model):
    owner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= 'tasks')
    title= models.CharField(max_length= 100)
    description= models.TextField(blank= True, null= True)
    is_done= models.BooleanField(default= False)

    def __str__(self):
        return self.title