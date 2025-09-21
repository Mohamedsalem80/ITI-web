from django.urls import path
from . import views, views_auth
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('create/', views.create_post, name='create_post'),

    # Auth
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html',
        authentication_form=CustomAuthenticationForm
    ), name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('register/', views_auth.register, name='register'),
]
