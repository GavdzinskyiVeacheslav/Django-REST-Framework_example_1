
from django.contrib import admin
from django.urls import path
from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenAPIList.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenAPIList.as_view()),
]

