from django.shortcuts import render,redirect
from .models import postmodel
from user_app.models import usermodel
from .forms import AddNewPostForm
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
    posts = postmodel.objects.filter(uploaded_by=user).order_by('-created')

    d={
        'user':user,
        'post':posts
    }
    return render(request,'photo_app/profile.html',d)


def addphoto(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid= request.session.get('user_id')
    user = usermodel.objects.filter(id=userid).first()
    if user:
        if request.method == 'POST':
            form = AddNewPostForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.uploaded_by = user
                post.save()
                return redirect('profile',user.username)
            else:
                return  render(request,'photo_app/add-photo.html',{'form':form})
        else:
            form =AddNewPostForm()
            d={
                'form' : form,
                'user': user
            }
            return render(request,'photo_app/add-photo.html',d)
    else:
        return redirect('index')
        

def delete_photo(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid= request.session.get('user_id')

    if request.method=='POST':
        postid = request.POST.get('postid',None)
        if postid:
            post = postmodel.objects.filter(id=postid,uploaded_by =userid).first()
            if post:
                post.delete()
        
    return redirect('index')


def search(request):
    if 'user_id' not in request.session:
        return redirect('login')

    if request.method == 'GET':
        query = request.GET.get('q',None)
        if query:
            userlist = usermodel.objects.filter(username__contains = query)
            d={
                'search_result':userlist
            }
            return render(request,'photo_app/search-result.html',d)
    return redirect('index')