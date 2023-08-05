from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    