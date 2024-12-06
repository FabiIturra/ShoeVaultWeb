from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('qr/', views.generate_qr, name='generate_qr'),
]