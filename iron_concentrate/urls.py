from django.urls import path, include

from iron_concentrate.views import IronConcentrateAPIView, MiddleIronConcentrateAPIView

urlpatterns = [
    path('iron_concentrate', IronConcentrateAPIView.as_view()),
    path('iron_concentrate/middle', MiddleIronConcentrateAPIView.as_view()),
]
