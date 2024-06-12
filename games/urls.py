from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game/<int:game_id>/review/', views.add_review, name='add_review'),
]
