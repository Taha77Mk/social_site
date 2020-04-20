"""social_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main_app.views import (pi,
                            PostListView, add_comment_to_post,
                            PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)
from users.views import register, loginpage, logoutuser, account, ProfileDetailView, updateprofile, ProfileCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('Post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('Post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('register/', register, name='register'),
    path('profile_update/<int:pk>/', updateprofile.as_view(), name='update_profile'),
    path('profile/new/', ProfileCreateView.as_view(), name='create_profile'),
    path('post/<int:pk>/comment/new', add_comment_to_post, name='add_comment_to_post'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('account/', account, name='account'),
    path('about/', pi, name='about'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
