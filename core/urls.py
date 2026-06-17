from rest_framework.routers import DefaultRouter

from core import viewsets

router = DefaultRouter()

router.register(prefix='state', viewset=viewsets.StateViewSet)
router.register(prefix='city', viewset=viewsets.CityViewSet)
router.register(prefix='zone', viewset=viewsets.ZoneViewSet)
router.register(prefix='district', viewset=viewsets.DistrictViewSet)

urlpatterns = router.urls


