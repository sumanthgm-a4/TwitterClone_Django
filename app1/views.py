from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from app1.models import Tweet

# Create your views here.

def render_home(request):
    all = Tweet.objects.all()[::-1]
    print(request.user)
    return render(request, "index.html", {"all": all})

def render_login(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.user)
    if request.user.is_authenticated:
        messages.warning(request, "You already logged in")
        return redirect('home')
    if request.method == "POST":
        a = request.POST.get("usern")
        b = request.POST.get("passw")
        print(a, b)
        result = User.objects.filter(username=a)
        print("User Exists? =", result)
        auth = authenticate(request, username=a, password=b)
        print("Valid Login Details? =", auth)
        if auth:
            login(request, auth)
            if request.user.is_superuser:
                print("Is Superuser")
                return redirect('/admin')
            messages.success(request, "You are successfully logged in")
            return redirect('home')
        else:
            return render(request, "login.html", {"res": "Please Enter Valid Credentials"})
    return render(request, "login.html", {"res": "Please Enter the Username and the Password"})

def render_register(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        password = request.POST.get('pword')
        cpassword = request.POST.get('cpword')
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('register')
        if len(password) < 8:
            messages.error(request, "Password must have 8 or more characters")
            return redirect('register')
        if password.isalnum():
            messages.error(request, "Password must have atleast one special character")
            return redirect('register')
        if password != cpassword:
            messages.error(request, "Passwords don't match")
            return redirect('register')
        new_user = User(username=username, first_name=firstname, last_name=lastname, email=email)
        new_user.set_password(password)
        new_user.save()
        messages.success(request, "User successfully created")
        return redirect('login')
    return render(request, "register.html")

@login_required(login_url="login")
def render_profile(request):
    print(request.user)
    if request.user.is_superuser:
        return redirect('admin/')
    n = len(Tweet.objects.filter(usern=request.user.username))
    return render(request, "profile.html", {'n': n})

def render_logout(request):
    logout(request)
    messages.info(request, "You are successfully logged out")
    return redirect('login')

@login_required(login_url="login")
def render_create_post(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            tweet = request.POST.get("tweet")
            obj = Tweet(usern=request.user, tweet=tweet)
            obj.save()
            messages.success(request, "Tweet successfully created")
            return redirect('home')
        else:
            messages.warning(request, "Please login to create a tweet")
            return redirect('login')
    return render(request, "tweet.html")

def render_display(request, post_id):
    t = Tweet.objects.get(id=post_id)
    if request.user.username == t.usern:
        print("Who tryna update:", request.user.username)
        print("Who can update:", t.usern)
        print(request.user.username == t.usern)
        if request.method == "POST":
            new_tweet = request.POST.get('tweet')
            t.tweet = new_tweet
            t.save()
            messages.success(request, "Tweet successfully updated")
            return redirect('home')
        return render(request, 'single.html', {"tweet": t})
    print("Likes:", t.likes.all())
    print("Dislikes:", t.dislikes.all())
    return render(request, "post.html", {"tweet": t})

def render_delete(request, post_id):
    obj = Tweet.objects.get(id=post_id)
    if request.user.is_superuser or (request.user.username == obj.usern):
        obj.delete()
        messages.success(request, "Tweet successfully deleted")
        return redirect('home')
    messages.error(request, f"You cannot delete @{obj.usern}'s tweets")
    return redirect('home')

@login_required(login_url="login")
def render_likes(request, post_id):
    post = Tweet.objects.get(id=post_id)
    if not post.dislikes.filter(username=request.user.username):
        post.likes.add(request.user)
    else:
        post.dislikes.remove(request.user)
        post.likes.add(request.user)
    return redirect("display", post_id=post_id)


@login_required(login_url="login")
def render_dislikes(request, post_id):
    post = Tweet.objects.get(id=post_id)
    if not post.likes.filter(username=request.user.username):
        post.dislikes.add(request.user)
    else:
        post.likes.remove(request.user)
        post.dislikes.add(request.user)
    return redirect("display", post_id=post_id)