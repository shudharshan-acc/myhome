from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .forms import UserRegisterationForm,UserLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")  # Redirect to a success page or homepage after registration
#     else:
#         form = UserCreationForm()  # Create a new form for GET requests

#     # Render the form in both POST failure and GET requests
#     return render(request, "security/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/manager/manage/')
    else:
        form = UserLoginForm()
        msg = " "
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is None:
                msg = "The username/password is incorrect"
            
            if user is not None:
                auth.login(request,user)
                return redirect('/manager/manage/')
    return render(request,'security/login.html',{'form':form,'msg':msg})


@login_required(login_url="/security/login/")
def logout_view(request):
    logout(request)
    return redirect('/security/login/')