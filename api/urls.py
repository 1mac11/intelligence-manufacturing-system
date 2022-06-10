from rest_framework.routers import SimpleRouter
from api import views

router = SimpleRouter()

router.register('territories', views.TerritoryViewSet)
router.register('statuses', views.StatusViewSet)
router.register('factory_types', views.FactoryTypeViewSet)
router.register('factories', views.FactoryViewSet)
router.register('buildings', views.BuildingViewSet)
router.register('building_types', views.BuildingTypeViewSet)
router.register('machine_tools', views.MachineToolViewSet)
router.register('machine_tool_types', views.MachineToolTypeViewSet)

urlpatterns = router.urls
