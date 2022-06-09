from rest_framework.routers import SimpleRouter
from api import views

router = SimpleRouter()

router.register('territory', views.TerritoryViewSet)
router.register('status', views.StatusViewSet)
router.register('factory_type', views.FactoryTypeViewSet)

urlpatterns = router.urls
