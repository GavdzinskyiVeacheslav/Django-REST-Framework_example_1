
from django.contrib import admin
from django.urls import path, include
from women.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), 
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]

