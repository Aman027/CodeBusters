from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

loggedin = 'false'

def signup_view(request):

    global loggedin

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            loggedin = 'true'
            login(request, user)
            return redirect('accounts:login_index')
    else:
        form = RegistrationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
        
        global loggedin

        if loggedin is 'true':
            return redirect('accounts:login_index')
    
        else:    
            if request.method == 'POST':
                form = LoginForm(data=request.POST)
                if form.is_valid():
                    #log the user in
                    user = form.get_user()
                    loggedin = 'true'
                    login(request, user)
                    return redirect('accounts:login_index') 

            else:
                form = LoginForm()
            return render(request, 'accounts/login.html', {'form':form})
    


@login_required(login_url='/accounts/login/')
def login_index(request):
    return render(request, 'accounts/loggedin.html')

def logout_view(request):
    global loggedin
    if request.method == 'POST':
        loggedin = 'false'
        logout(request)
        return redirect('accounts:home')

def home(request):
    global loggedin

    if loggedin is 'true':
        return redirect('accounts:login_index')

    else:
        return render(request, 'accounts/homepage.html')

# Create your views here.
