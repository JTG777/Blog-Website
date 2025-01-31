from django.shortcuts import render,redirect
from .forms import PostForm,CommentsForm
from .models import Post,Tag,Category,Like
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    post_list=Post.objects.filter(published=True).order_by('-updated_at')
    
    #for blog search functionality
    item=request.GET.get('input-search')
    if item != '' and item is not None:
        post_list=Post.objects.filter(title__icontains=item)

    context={'post_list':post_list}
    return render(request,'blog/index.html',context)
    
#normal function 
def string_to_tags(tag_string):
    tags=[tag.strip().lower() for tag in tag_string.split(',') if tag.strip()]
    
    return tags
    

@login_required
def add_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post_obj=form.save(commit=False)
            post_obj.author=request.user
            post_obj.save()
            tag_string=form.cleaned_data.get('tag_input')
            if tag_string:
                tags=string_to_tags(tag_string)
                print(type(tags))
                for tag in tags:
                    tag_obj,created=Tag.objects.get_or_create(name=tag)
                    post_obj.tag.add(tag_obj)

                

            return redirect('blog:index')
    form=PostForm()
    context={'form':form}
    return render(request,'blog/add_post.html',context)

@login_required
def edit_post(request,blog_id):
    # instance=Post.objects.get(id=blog_id)
    instance=get_object_or_404(Post,id=blog_id)
    if instance.author!=request.user:
        raise Http404
    if request.POST:
        form=PostForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            post_obj=form.save()
            tag_string=form.cleaned_data['tag_input']
            print(tag_string)
            if tag_string:
                tags=string_to_tags(tag_string)
                for tag in tags:
                    tag_obj,created=Tag.objects.get_or_create(name=tag)
                    post_obj.tag.add(tag_obj)


            return redirect('blog:index')
    else:
        tag_string=', '.join(instance.tag.values_list('name',flat=True))
        form=PostForm(instance=instance,initial={'tag_input':tag_string})
        context={'form':form}
        return render(request,'blog/edit_post.html',context)


def view_post(request, slug):
    instance = get_object_or_404(Post, slug=slug)  # More efficient than `.get()`
    
    comment_form = CommentsForm(request.POST or None)  # More efficient form handling
    
    if request.method == "POST" and comment_form.is_valid():
        comment_obj = comment_form.save(commit=False)
        comment_obj.post = instance
        comment_obj.author = request.user
        comment_obj.save()
        return redirect('blog:view_post', slug=slug)  # PRG Pattern to prevent duplicate submission

    context = {
        'post': instance,
        'comment_form': comment_form,
        'comments': instance.comments.all(),
        'tags': instance.tag.all(),
        'like_count': instance.likes.count()  # More efficient count retrieval
    }
    
    return render(request, 'blog/view_post.html', context)
@login_required
def delete_post(request,blog_id):

    instance=Post.objects.get(id=blog_id)
    if instance.author!=request.user:
        raise Http404

    instance.delete()
    return redirect('blog:index')

def view_category_post(request,slug):
    category=Category.objects.get(slug=slug)
    posts=category.posts.filter(published=True).order_by('-updated_at')
    context={'category':category,'posts':posts}
    return render(request,'blog/category_page.html',context)

@login_required
def like_post(request,blog_id):
    instance=Post.objects.get(id=blog_id)
    if not Like.objects.filter(user=request.user,post=instance).exists():
        Like.objects.create(user=request.user,post=instance)
    return redirect('blog:view_post',slug=instance.slug)


    

