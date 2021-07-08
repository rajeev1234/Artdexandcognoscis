from django.urls import path, include
from rest_framework import routers
from makerChecker import views

router = routers.DefaultRouter()
router.register(r'make', views.MakeViewSet,basename='Make')
router.register(r'model', views.ModelsViewSet,basename='Model')
router.register(r'variant', views.VariantViewSet,basename='Variant')
router.register(r'allDetails', views.ViewAllVariantDetailViewSet,basename='allDetails')

makerChecker_urls = [
    path('', include(router.urls)),
]