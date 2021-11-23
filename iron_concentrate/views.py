from decimal import Decimal

from django.db.models import F, Count, Max
from rest_framework import generics

from iron_concentrate.models import IronConcentrate
from iron_concentrate.serializers import IronConcentrateSerializer


class IronConcentrateAPIView(generics.ListCreateAPIView):
    queryset = IronConcentrate.objects.annotate(avg_iron=F('iron') * Decimal('1.0') / IronConcentrate.objects.count(),
                                                max=Max('iron'))
    serializer_class = IronConcentrateSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = StatisticsFilter
