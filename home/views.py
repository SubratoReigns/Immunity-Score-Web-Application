from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post
from models.models import Patient, DiabetesPatient

def home(request):
    return render(request, 'home/index.html')

 

def contact(request):

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<3 or len(email)<11 or len(phone)<10 or len(content)<6:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent!")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']

    if len(query)>73:
        allPosts = Post.objects.none()

    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
        messages.warning(request, "No search results found! Please refine your query.")
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must contain characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been created successfully!!")    
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
        if request.method == 'POST':
            # Get the post parameter
            loginusername = request.POST['loginusername']
            loginpass = request.POST['loginpass']
            user = authenticate(username=loginusername, password=loginpass)

            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")

                

                
                return redirect('/model')

            else:
                messages.error(request, "Invalid credentials, Please try again")
                return redirect('home')

        return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')







