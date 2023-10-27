from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect, redirect
from . models import Users1,CustomUser
from apps . forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from . manager import CustomManager




# Create your views here.

def show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pp=fm.cleaned_data['password']
            print(request.user)
            reg=Users1(name=nm,email=em,password=pp,author = request.user)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    if request.user.is_superuser:  # Check if the user is a superuser
        stud = CustomUser.objects.all()  # Show all users from the User model
        return render(request,"enroll/admin.html",{'form':fm,'stu':stud})
    elif request.user.is_floor_manager:
        stud = CustomUser.objects.filter(groups__name='FM')
        return render(request,"enroll/admin.html",{'form':fm,'stu':stud})

    elif request.user.is_team_lead:
        fm = CustomUser.objects.filter(groups__name='TL')
    elif request.user.is_team_member:
        fm = CustomUser.objects.filter(groups__name='TM')

    else:
        stud = Users1.objects.filter(author=request.user) 
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#This Function will return Update data



def detailsdata(request):
    user = request.user
    is_admin = user.is_superuser
    user_role = user.status

    # Query users based on their roles
    fm_users = CustomUser.objects.filter(status='FM')
    tl_users = CustomUser.objects.filter(status='TL')
    tm_users = CustomUser.objects.filter(status='TM')
    tr_users = CustomUser.objects.filter(status='TR')
    print(user_role)
    context = {
        'is_admin': is_admin,
        'user_role': user_role,
        'is_floor_manager': fm_users,
        'is_team_lead': tl_users,
        'is_team_member': tm_users,
        'tr_users': tr_users,
    }

    return render(request, 'organization/list.html', context)

def update(request,id):
    if request.method=='POST':
        pi=Users1.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Users1.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    return render(request,'enroll/update.html',{'form':fm})

#This Will return Delete data

def deletedate(request,id):
    if request.method=='POST':
        pi=Users1.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

# **************************************** User Registration ***********************************

def userregistration(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=RegistrationForm(request.POST)
            if fm.is_valid():
                fname = fm.cleaned_data['first_name']
                lname = fm.cleaned_data['last_name']
                em=fm.cleaned_data['email']             
                ss=fm.cleaned_data['status']             
                # userforfm = CustomUser(first_name=fname, last_name=lname, email=em,status=ss)
                # userforfm.save()
                user=fm.save()
                if ss == 'FM':
                    group = Group.objects.get(name='FM')
                    user.groups.add(group)
                elif ss == 'TL':
                    group = Group.objects.get(name='TL')
                    user.groups.add(group)
                elif ss == 'TM':
                    group = Group.objects.get(name='TM')
                    user.groups.add(group)
                return HttpResponse("Registration submit")
        else:
            fm=RegistrationForm()
        return render(request,"enroll/registration.html",{'form':fm})

    else:
        return HttpResponseRedirect('details/')

# **************************************** Login ***********************************

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Login Successfull')
                    return redirect(detailsdata)
        else:
            form=loginform()
        return render(request,'enroll/login.html',{"form":form})
    else:
        return HttpResponseRedirect('detailsdata/')


# def dashboard(request):
#     if request.user.is_authenticated:
#         posts = Users1.objects.all()
#         user = request.user
#         full_name = user.get_full_name()
#         gps = user.groups.all()
#         return render(request,'dashboard.html',{"posts":posts,"fullname":full_name,"groups":gps})
#     else:
#         return redirect(user_login)

# **************************************** Logout ***********************************

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



# **************************************** Admin Delete ***********************************


def admindelete(request,id):
    if request.method=='POST':
        pi=CustomUser.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

# **************************************** Admin Edit ***********************************


def adminupdate(request, id):
    if request.method == 'POST':
        user = CustomUser.objects.get(pk=id)
        fm = EditAdminUserProfileForm(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Login Successfull')
            return redirect(show)
    else:
        user = CustomUser.objects.get(pk=id)
        fm = EditAdminUserProfileForm(instance=user)

    return render(request, 'enroll/update.html', {'form': fm})

