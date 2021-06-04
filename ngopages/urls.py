from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'ngopages'

urlpatterns = [
    path('', Mainpageview.as_view(), name='mainpage'),

    path('ngo/', Indexview.as_view(), name='index'),
    path('login/', Loginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=('ngopages:login')), name='logout'),
    path('register/', Registerview.as_view(), name='register'),
    path('addactivity/', AddActivityview.as_view(), name='addactivity'),
    path('<slug:slug>/editactivity/', EditActivityview.as_view(), name='editactivity'),
    path('<slug:slug>/editprofile/', EditProfileview.as_view(), name='editngoprofile'),
    path('<slug:slug>/deleteactivity', DeleteActivityview.as_view(), name='deleteactivity'),

    path('user/', UserIndexview.as_view(), name='userindex'),
    path('user/povertycare/', Povertycareview.as_view(), name='povertycare'),
    path('user/hungerrelief/', Hungerreliefview.as_view(),name='hungerrelief'),
    path('user/healthcare/',Healthcareview.as_view(),name='healthcare'),
    path('user/educationalaids/',Educationalaidsview.as_view(),name='educationalaids'),
    path('user/<slug:slug>/ngodetail',Ngodetailview.as_view(),name='ngodetail'),
]