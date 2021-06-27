from rest_framework.routers import DefaultRouter
from .views import SchoolModuleViewSet

router = DefaultRouter()
router.register(r"", SchoolModuleViewSet)

urlpatterns = router.urls
