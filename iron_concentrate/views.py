from decimal import Decimal

import pandas as pd
from django.db.models import F, Count, Max
from rest_framework import generics, status
from rest_framework.response import Response

from iron_concentrate.base.services import get_obj_list
from iron_concentrate.models import IronConcentrate
from iron_concentrate.serializers import IronConcentrateCreateSerializer, IronConcentrateListSerializer


class SerializerByMethodMixin:
    """choosing serializer for method"""

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class IronConcentrateAPIView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = IronConcentrate.objects.annotate(avg_iron=F('iron') * Decimal('1.0') / IronConcentrate.objects.count(),
                                                max=Max('iron'))
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = StatisticsFilter

    serializer_map = {
        'GET': IronConcentrateListSerializer,
        'POST': IronConcentrateCreateSerializer,
    }

    def create(self, request, *args, **kwargs):
        print(request)
        if isinstance(request, list):
            for i in request:
                serializer = self.get_serializer(data=i)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        if request.data['file_excel']:
            excel = get_obj_list(request.data['file_excel'])
            # print(excel)
            return self.create(excel, *args, **kwargs)
        return self.create(request, *args, **kwargs)
