from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # home(main page) -> ex)127.0.0.1:[port]
    path('', views.HomeView.as_view(), name = 'home'),

    path("admin/", admin.site.urls),
    path("users/",include('users.urls')),
]
