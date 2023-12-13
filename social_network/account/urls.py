from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views
from .views import user_login, dashboard, register, edit, user_list, user_detail, user_follow

#app_name = 'account'

urlpatterns = [
    #path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(
    #     success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #     success_url=reverse_lazy('account:password_reset_done')), name='password_reset'
    # ),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')),
    #      name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('users/', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<username>/', user_detail, name='user_detail')
]
