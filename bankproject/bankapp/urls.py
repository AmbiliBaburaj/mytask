from . import views
from django.urls import path
app_name='bankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('biodata/',views.register,name='biodata'),
    ]