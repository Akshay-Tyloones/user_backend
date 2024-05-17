from django.urls import path 
from .views import signup, verify_email,get_all_users, disconnect
from .views import ConnectView,SubscribeView,UserDetailsView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('verify-email/', verify_email, name='verify_email'),
    path('user-details/', get_all_users, name ='get_all_users' ),
    # path('connect/', connect, name ='connect' ),
    path('connect/', ConnectView.as_view(), name='connect'),
    path('disconnect/', disconnect, name ='disconnect' ),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('user-data/', UserDetailsView.as_view(), name='user_data'),
    
]