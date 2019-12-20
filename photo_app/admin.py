from django.contrib import admin

from .models import postmodel,commentsmodel
# Register your models here.
admin.site.register(postmodel)
admin.site.register(commentsmodel)

