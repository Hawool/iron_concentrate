from django.urls import path, include

from iron_concentrate.views import IronConcentrateAPIView

urlpatterns = [
    path('iron_concentrate', IronConcentrateAPIView.as_view()),
]
