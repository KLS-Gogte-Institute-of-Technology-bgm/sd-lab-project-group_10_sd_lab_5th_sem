from django.core.checks import messages
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from .forms import ProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.decorators import login_required
from .models import Profile
from ticket.models import Ticket
# Create your views here.




@unauthenticated_user
def registerPage(request):
    if request.method == "POST":
        username = request.POST['user_name'].upper()
        email = request.POST['email'].upper()
        phone = request.POST['phone_number']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        try:
            if pass1==pass2 and len(pass1)>8:
                if not User.objects.filter(email=email):
                    myuser = User.objects.create_user(username,email,pass1)
                    user = myuser
                    group = Group.objects.get(name='customer')
                    user.groups.add(group)
                    myuser.save()
                    Profile.objects.create(
                        user=myuser,
                        phone = phone
                    )
                    return redirect('loginPage')
                else:
                    return render(request,'basic/register.html',{'messages':'Email  is not unique please check '})
            else:
                return render(request,'basic/register.html',{'messages':'password is not same or password length is small'})
        except Exception as e:
            return render(request,'basic/register.html',{'messages':'Please enter unique username'})
    return render(request,'basic/register.html')


@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username = request.POST['username'].upper()
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/ticket')
        else:
            messages.info(request,'Username or password is incorrect')
            return render(request,'basic/login.html')
    return render(request,'basic/login.html')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['manager','watchman','customer','admin'])
def logoutPage(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user = user)
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile) 
        if form.is_valid():
            form.save()
            messages.info(request,'successfully updated profile')
    return render(request,'basic/user.html',{'form':form,'user':user})

@login_required(login_url='/login')
@allowed_users(allowed_roles=['customer'])
def myTicket(request):
    user = request.user
    profile = Profile.objects.get(user=user).phone
    ticket = Ticket.objects.filter(phone_number=profile)
    return render(request,'basic/myticket.html',{'ticket':ticket})