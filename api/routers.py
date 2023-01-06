from rest_framework.routers import DefaultRouter
from .views import PhotoCreateView

router = DefaultRouter()
router.register("photos", PhotoCreateView)

