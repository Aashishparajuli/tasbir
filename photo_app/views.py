from django.shortcuts import render,redirect
from .models import postmodel
from user_app.models import usermodel
# Create your views here.
def index(request):
    if 'user_id' in request.session:
        allpost = postmodel.objects.all().order_by('-created')
        d={
            'posts' : allpost
        }
        return render(request,'photo_app/index.html',d)
    else:
        return redirect('login')


def profile(request , username ):

    user= usermodel.objects.filter(username=username).first()

    d={
        'user':user
    }
    return render(request,'photo_app/profile.html',d)

