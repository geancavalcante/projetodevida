
from django.urls import path, include
from blog import views

urlpatterns = [
    path('',views.home, name='home'),
    path('pagina/',views.pagina, name='pagina'),
]