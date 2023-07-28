from django.urls import path
from Lectores import views
from django.contrib.auth.views import LogoutView 

app_name = "Lectores"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='lectores/login.html'), name='logout'),
    path('registro/', views.registrarse, name='registrarse')
]

    