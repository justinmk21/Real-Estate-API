from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, PropertyListCreate, PropertyDetail, ContactCreate, AgentList

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('properties/', PropertyListCreate.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
    path('agents/', AgentList.as_view(), name='agent-list'),
    path('contact/', ContactCreate.as_view(), name='contact-create'),
]
