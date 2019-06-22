from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

loggedin = 'false'

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def signup_index(request):
    return HttpResponse("You are signed up")

def login_view(request):
        
        global loggedin

        if loggedin is 'true':
            return redirect('accounts:login_index')
    
        else:    
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)
                if form.is_valid():
                    #log the user in
                    user = form.get_user()
                    loggedin = 'true'
                    login(request, user)
                    return redirect('accounts:login_index') 

            else:
                form = AuthenticationForm()
            return render(request, 'accounts/login.html', {'form':form})
    


@login_required(login_url='/accounts/login/')
def login_index(request):
    return render(request, 'accounts/loggedin.html')

def logout_view(request):
    global loggedin
    if request.method == 'POST':
        loggedin = 'false'
        logout(request)
        return redirect('accounts:login')

# Create your views here.
