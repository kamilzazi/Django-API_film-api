from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import FilmViewset

router = routers.DefaultRouter()
router.register('filmy', FilmViewset)

urlpatterns = [
    path('', include(router.urls)),
]
