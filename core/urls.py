from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('check_paragraph/', views.check_paragraph, name="check_paragraph")
]
