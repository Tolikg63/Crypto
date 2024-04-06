from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('how/', views.How.as_view(), name='how'),
    path('about/', views.About.as_view(), name='about'),
]
