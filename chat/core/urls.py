from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, SignUpView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('chats/', choosechat, name='chats'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
