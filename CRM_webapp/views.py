from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You Have Successfully Registered")
            return redirect("user_login")

    else:
        form=SignUpForm()
        return render(request,"signup.html",{"form":form})
    return render(request,"signup.html",{"form":form})
def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.success(request,"You Are Not Signed In,Please Create An Acount")
            return redirect("user_login")
    else:
      return render(request,"user_login.html")
    
def user_logout(request):
    logout(request)
    return redirect("home")
def dashboard(request):
    records=Record.objects.all()
    return render(request,"dashboard.html",{"records":records})


def user_record(request,pk):
      if request.user.is_authenticated:
          user_record=Record.objects.get(id=pk)
          return render(request,'record.html',{"user_record":user_record})
      else:
          return redirect("home")

def back_to_records(request):
    return redirect('dashboard')


def delete_record(request,pk):
    record_to_delete=Record.objects.get(id=pk)
    record_to_delete.delete()
    messages.success(request,"Record Deleted Successfully")
    return redirect('dashboard')

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid:
                add_record=form.save()
                messages.success(request,"Record Added")
                return redirect('dashboard')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You Must Be Logged In")
        return redirect("user_login")


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Updated")
            return redirect('dashboard')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"You Must Log In")
        return redirect('dashboard')