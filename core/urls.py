from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('signup/', views.signup, name='signup'),

    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('add/', views.add_note, name='add_note'),
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),

]