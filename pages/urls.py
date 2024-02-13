from django.urls import include, path 
from .views import homePageView 

urlpatterns = [ 
    path("", homePageView, name='home') ,
    path("", include('pages.urls')),
] 