from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import JobViewSet

router = SimpleRouter()
router.register('', JobViewSet, basename='jobs')

urlpatterns = router.urls