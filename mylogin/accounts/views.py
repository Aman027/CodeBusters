from django.shortcuts import render, redirect
from accounts.forms import(
    BuyerRegistrationForm,
    SellerRegistrationForm,
    LoginForm,
    EditProfileForm
)
from django.http import HttpResponse
from django.contrib.auth import(
    login,
    logout,
    authenticate,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

loggedin = 'false'

def buyer_signup_view(request):

    global loggedin

    if loggedin is 'true':
            return redirect('accounts:login_index')

    else:
        if request.method == 'POST':
            form = BuyerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                loggedin = 'true'
                login(request, user)
                return redirect('accounts:login_index')
        else:
            form = BuyerRegistrationForm()
        return render(request,'accounts/buyersignup.html',{'form':form})


def seller_signup_view(request):

    global loggedin

    if loggedin is 'true':
            return redirect('accounts:login_index')

    else:
        if request.method == 'POST':
            form = SellerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                loggedin = 'true'
                login(request, user)
                return redirect('accounts:login_index')
        else:
            form = SellerRegistrationForm()
        return render(request,'accounts/sellersignup.html',{'form':form})        

def login_view(request):
        
        global loggedin

        if loggedin is 'true':
            return redirect('accounts:login_index')
    
        else:    
            if request.method == 'POST':
                form = LoginForm(data=request.POST)
                if form.is_valid():
                    user = form.get_user()
                    loggedin = 'true'
                    login(request, user)
                    return redirect('accounts:login_index') 

            else:
                form = LoginForm()
            return render(request, 'accounts/login.html', {'form':form})


def my_profile(request):
    return render(request, 'accounts/myprofile.html',{'user':request.user})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:my_profile')

    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/editprofile.html',{'form':form})
    


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

def signup_options(request):
    return render(request, 'accounts/options.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:my_profile')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/changepassword.html',{'form':form})


# Create your views here.
