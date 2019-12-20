from django.db import models
from user_app.models import usermodel

# Create your models here.

class postmodel(models.Model):
    created      = models.DateTimeField(auto_now_add= True)
    location     = models.CharField(max_length=255)
    photo        = models.ImageField(upload_to='user_uploads')
    likes        = models.PositiveIntegerField( default = 0)
    uploaded_by  = models.ForeignKey(usermodel, on_delete=models.CASCADE)
    liked_by     = models.ManyToManyField(usermodel, related_name='liked_photos',blank=True)


    def __str__(self):
        return str(self.created)

class commentsmodel(models.Model):
    commenttime   = models.DateTimeField(auto_now_add=True)
    commenttext   = models.TextField()
    commentedby   = models.ForeignKey(usermodel , on_delete=models.CASCADE)
    commentpostby = models.ForeignKey(postmodel,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.commenttime)
