from decimal import Decimal

import django_filters
from django.db.models import F, Count, Max, Avg, Min, Value
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from iron_concentrate.base.services import get_obj_list
from iron_concentrate.models import IronConcentrate
from iron_concentrate.serializers import IronConcentrateCreateSerializer, IronConcentrateListSerializer, \
    MiddleIronConcentrateSerializer


class SerializerByMethodMixin:
    """choosing serializer for method"""

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


# class MonthFilter(django_filters.FilterSet):
#     """class for filter"""
#     class Meta:
#         model = IronConcentrate
#         fields = {
#             'month': ['iexact', 'lte', 'gte'],
#         }


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
            serializer = self.get_serializer(data=request, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # print(serializer.data)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        if 'file_excel' in request.data.keys():
            excel = get_obj_list(request.data['file_excel'])
            return self.create(excel, *args, **kwargs)
        return self.create(request, *args, **kwargs)


class MiddleIronConcentrateAPIView(generics.GenericAPIView):
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = MonthFilter
    # filter_fields = ['gender', 'first_name', 'last_name']

    serializer_class = MiddleIronConcentrateSerializer
    # def get(self, request):
    #     queryset = IronConcentrate.objects.annotate(
    #         middle=Value(IronConcentrate.objects.aggregate(Avg('iron'))['iron__avg'],
    #                      output_field=models.FloatField()),
    #         max=Value(IronConcentrate.objects.aggregate(Max('iron'))['iron__max'],
    #                      output_field=models.FloatField()),
    #         min=Value(IronConcentrate.objects.aggregate(Min('iron'))['iron__min'],
    #                        output_field=models.FloatField())
    #     )
    #     serializer = MiddleIronConcentrateSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        queryset = IronConcentrate.objects.filter(month=request.data['month']).annotate(
            middle=Value(IronConcentrate.objects.filter(month=request.data['month']).aggregate(Avg('iron'))['iron__avg'],
                         output_field=models.FloatField()),
            max=Value(IronConcentrate.objects.filter(month=request.data['month']).aggregate(Max('iron'))['iron__max'],
                      output_field=models.FloatField()),
            min=Value(IronConcentrate.objects.filter(month=request.data['month']).aggregate(Min('iron'))['iron__min'],
                      output_field=models.FloatField())
        )
        if not queryset:
            return Response([])

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])
