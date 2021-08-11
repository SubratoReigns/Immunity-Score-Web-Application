from django.shortcuts import render, HttpResponse,redirect
from blog.models import Post, Usercomment
from django.contrib import messages

def blogh(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blog.html', context)

def blogp(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Usercomment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/blogpost.html', context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        
        comment = Usercomment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully!!")

    return redirect("/blog/{post.slug}")


    
