from django.urls import path
from Lectores import views

app_name = "Lectores"

urlpatterns = [
    path('login/', views.login, name='login')
]

    