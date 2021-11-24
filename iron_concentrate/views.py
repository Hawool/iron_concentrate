from decimal import Decimal

from django.db.models import F, Max, Avg, Min
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response

from iron_concentrate.base.services import get_obj_list
from iron_concentrate.models import IronConcentrate
from iron_concentrate.serializers import IronConcentrateSerializer, MiddleIronConcentrateSerializer


class SerializerByMethodMixin:
    """choosing serializer for method"""

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)


class IronConcentrateAPIView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = IronConcentrate.objects.all()
    serializer_map = {
        'GET': IronConcentrateSerializer,
        'POST': IronConcentrateSerializer,
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
    serializer_class = IronConcentrateSerializer

    def post(self, request, *args, **kwargs):
        queryset = IronConcentrate.objects.filter(month=request.data['month'])

        if not queryset:
            return Response([])

        queryset = self.filter_queryset(queryset)

        middle = queryset.aggregate(Avg('iron'))['iron__avg']
        max = queryset.aggregate(Max('iron'))['iron__max']
        min = queryset.aggregate(Min('iron'))['iron__min']

        data = {
            "month": request.data['month'],
            "middle": str(middle),
            "max": str(max),
            "min": str(min)
        }

        return JsonResponse(data, status=status.HTTP_200_OK)
