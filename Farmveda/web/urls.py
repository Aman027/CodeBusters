from django.urls import include, path

urlpatterns = [
    path('search/',include('haystack.urls')),
]