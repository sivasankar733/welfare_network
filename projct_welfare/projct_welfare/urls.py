"""projct_welfare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_wlfare import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showindex.as_view(), name='index'),
    path('adminlog/', views.adminloging.as_view(), name='adminlog'),
    path('registeruser/', views.RegisterUser.as_view(), name='registeruser'),
    path('addthoughts/', views.AddThoughts.as_view(), name='addthoughts'),
    path('viewthoughts/', views.ViewThoughts.as_view(), name='viewthoughts'),
    path('addevents/', views.AddEvents.as_view(), name='addevents'),
    path('viewevents/', views.ViewEvents.as_view(), name='viewevents'),
    path('technicaladd/', views.TechnicalAdd.as_view(), name='technicaladd'),
    path('viewtechnical/', views.ViewTechnical.as_view(), name='viewtechnical'),
    path('workexperience/', views.WorkExperience.as_view(), name='workexperience'),
    path('viewworkexperience/', views.ViewWorkExperience.as_view(), name='viewworkexperience'),
    path('property/', views.AddProperty.as_view(), name='property'),
    path('viewproperty/', views.ViewProperty.as_view(), name='viewproperty'),
    path('addsharemarket/', views.AddShareMarket.as_view(), name='addsharemarket'),
    path('viewsharemarket/', views.ViewShareMarket.as_view(), name='viewsharemarket'),
    path('addreference/', views.AddReference.as_view(), name='addreference'),
    path('viewreference/', views.ViewReferences.as_view(), name='viewreference'),
    path('addmatrimonial/', views.AddMatrimonial.as_view(), name='addmatrimonial'),
    path('viewmatrimonial/', views.ViewMatrimonial.as_view(), name='viewmatrimonial'),
    path('addcelebrations/', views.AddCelebrations.as_view(), name='addcelebrations'),
    path('viewcelebrations/', views.ViewCelebrations.as_view(), name='viewcelebrations'),
    path('addtravel/', views.AddTravel.as_view(), name='addtravel'),
    path('viewtravel/', views.ViewTravel.as_view(), name='viewtravel'),
    path('approval/', views.approvaldetails, name='approval'),
    path('accept/',views.accept_user,name='accept'),
    path('reject/',views.reject_user,name='reject'),
    path('show_accept/',views.show_accept_user,name='show_accept'),
    path('show_reject/',views.show_reject_user,name='show_reject'),

]
