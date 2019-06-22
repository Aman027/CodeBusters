from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signedup/', views.signup_index , name='signup_index'), 
    path('login/', views.login_view , name='login'), 
    path('loggedin/', views.login_index , name='login_index'),
    path('logout/', views.logout_view, name='logout')
]