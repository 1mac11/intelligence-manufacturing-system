from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api import views
from api.views import RegisterView, AccessTokenView, LogoutView

router = SimpleRouter()

router.register('territories', views.TerritoryViewSet)
router.register('statuses', views.StatusViewSet)
router.register('factory_types', views.FactoryTypeViewSet)
router.register('factories', views.FactoryViewSet)
router.register('buildings', views.BuildingViewSet)
router.register('building_types', views.BuildingTypeViewSet)
router.register('machine_tools', views.MachineToolViewSet)
router.register('machine_tool_types', views.MachineToolTypeViewSet)
router.register('users', views.UserViewSet)
router.register('teams', views.TeamViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
    path('token/', AccessTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Uncomment if you want to check token to HMAC
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('logout/', LogoutView.as_view(), name='register-user'),

]

urlpatterns += router.urls
