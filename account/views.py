from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    if request.method == 'POST' :
        form = LoginForm(request=request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,'account.html',{'form':form})



    else : 
        form =LoginForm()
        return render(request,'account.html',{'form':form})

def logout_view(req):
    logout(req)
    return redirect('home')

def register(req):
    if req.method == 'POST' : 
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect('home')
        return render(req,'account.html',{'form':form})

            
    else : 
        form =RegisterForm()
        return render(req,'account.html',{'form':form})
        
@property
def get_grade(self):
    if(user.point>10) :
        user.grade = '브론즈'
        user.save()
# Create your views here.

