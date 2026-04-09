from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ApplicationViewSet

router = SimpleRouter()
router.register('', ApplicationViewSet, basename='applications')

urlpatterns = router.urls