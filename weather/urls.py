from django.urls import path 
from .views import signup, verify_email,get_all_users

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify-email/<str:email>/', verify_email, name='verify_email'),
    path('user-details/', get_all_users, name ='get_all_users' )
]