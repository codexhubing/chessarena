from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('<int:pk>/', views.game_view, name='detail'),
]