from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, TournamentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('games', GameViewSet)
router.register('tournaments', TournamentViewSet)

urlpatterns = [
    path('v1/auth/', obtain_auth_token),
    path('v1/', include(router.urls)),
]