from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet

router = DefaultRouter()
router.register(r"", ParticipantViewSet)

urlpatterns = router.urls
