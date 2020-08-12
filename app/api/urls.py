from django.urls import path
from rest_framework import routers

from .views import *

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'urls', UrlViewSet, basename='url')
router.register(r'keys', KeyViewSet, basename='key')

urlpatterns = [
    path('', api_root),
]

urlpatterns += router.urls
