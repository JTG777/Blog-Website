from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Profile
from blogs.models import Post
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect('blog:index')
        return render(request,'registration/register.html')
    else:
        form=UserCreationForm()
        context={'form':form}
        return render(request,'registration/register.html',context)

@login_required    
def profile(request):
    profile=Profile.objects.get(user=request.user)
    context={'profile':profile}
    return render(request,'profile.html',context)

@login_required    
def profile_blogs(request):
    profile=Profile.objects.get(user=request.user)
    #for draft blogs
    draft_blogs=profile.user.posts.filter(published=False)
    # for published blogs
    published_blogs=Post.objects.filter(author=profile.user,published=True)

    context={'draft_blogs':draft_blogs,'profile':profile,'published_blogs':published_blogs}


    return render(request,'profile_blogs.html',context)

@login_required    
def edit_profile(request):
    instance=Profile.objects.get(user=request.user)
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:

        form=ProfileForm(instance=instance)
       
    return render(request,'edit_profile.html',{'form':form})


def publish_now(request,blog_id):
    blog=Post.objects.get(id=blog_id)
    blog.published=True
    blog.save()
    return redirect('accounts:profile_blogs')