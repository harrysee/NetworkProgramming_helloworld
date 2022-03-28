from django.contrib import admin
from django.urls import path, include

from bossbaby import views

app_name ="bossbaby"

urlpatterns = [
    path('boss/', views.show_boss, name="profile"),
    path('templten/',views.show_templten, name="job"),
]
