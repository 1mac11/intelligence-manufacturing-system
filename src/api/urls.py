from rest_framework.routers import SimpleRouter
from api import views

router = SimpleRouter()

router.register('territory', views.TerritoryViewSet)

urlpatterns = router.urls
