from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),

    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(template_name="authentication/password_change_done.html")),

    path('password-reset/',
         PasswordResetView.as_view(
             template_name="authentication/password_reset_form.html",
             email_template_name="authentication/password_reset_email.html",
             success_url=reverse_lazy("authentication:password_reset_done")
         ),
         name='password_reset'),

    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name="authentication/password_reset_done.html",
         ),
         name="password_reset_done"),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="authentication/password_reset_confirm.html",
             success_url=reverse_lazy("authentication:password_reset_complete")
         ),
         name='password_reset_confirm'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name="authentication/password_reset_complete.html"
         ),
         name='password_reset_complete'),
]
