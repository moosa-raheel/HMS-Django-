from django.shortcuts import render, redirect
from account.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login

# Home View 
def home(request):
    return render(request,"base.html")

# Login View 
def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.values()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
    else:
        form = LoginForm(auto_id=True)
    return render(request,"login.html", {"form":form})

# Signup View 
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form" : form})