from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEdit,ProfileEdit
from posts.models import Post
# Create your views here.
def user_login(request):

    if request.method == "POST":
        form=LoginForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('invalid login credatials')
    else:
        form = LoginForm()

    return render(request,'users/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def index(request):
    current_user=request.user

    user_post=Post.objects.filter(user=current_user)

    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'users/index.html',{'user_post':user_post,'profile':profile})


def user_registration(request):

    if request.method=="POST":
        user_form=RegisterationForm(request.POST)

        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'users/register_done.html')
    else:
        user_form=RegisterationForm()

    return render(request,'users/register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method =='POST':
        user_form=UserEdit(instance=request.user,data=request.POST)
        profile_form=ProfileEdit(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form=UserEdit(instance=request.user)
        profile_form=ProfileEdit(instance=request.user.profile,)
    return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})