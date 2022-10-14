from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/' , views.register , name='register'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
    path('message/' , views.add_message , name='message'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    path('dashboard/saved/<int:pk>' , views.save_course , name='saved'),
    path('dashboard/deleted/<int:pk>' , views.delete_course , name='deleted'),
    path('dashboard/update_profile',views.update_profile,name='update_profile')
]
