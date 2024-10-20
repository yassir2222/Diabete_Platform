
from django.urls import path
from . import views
from .views import send_message, list_messages
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('main/',views.main,name="main"),
    path('send', send_message, name='send_message'),
    path('chat/', list_messages, name='list_messages'),
]
