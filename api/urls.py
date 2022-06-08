from rest_framework.routers import SimpleRouter
from api.views import territory

router = SimpleRouter()

router.register('territory', territory.TerritoryViewSet)

urlpatterns = router.urls
