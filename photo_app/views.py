from django.shortcuts import render
from .models import postmodel
# Create your views here.
def index(request):

    allpost = postmodel.objects.all()
    d={
        'posts' : allpost
    }

    return render(request,'photo_app/index.html',d)


