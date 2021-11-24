from rest_framework import serializers

from iron_concentrate.models import IronConcentrate


class IronConcentrateListSerializer(serializers.ModelSerializer):
    avg_iron = serializers.DecimalField(max_digits=10, decimal_places=5)
    max = serializers.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        model = IronConcentrate
        fields = '__all__'


class IronConcentrateCreateSerializer(serializers.ModelSerializer):
    # file_excel = serializers.FileField()

    class Meta:
        model = IronConcentrate
        fields = ['name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month']


class MiddleIronConcentrateSerializer(serializers.ModelSerializer):
    middle = serializers.DecimalField(max_digits=10, decimal_places=3)
    min = serializers.DecimalField(max_digits=10, decimal_places=3)
    max = serializers.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        model = IronConcentrate
        fields = ['month', 'middle', 'min', 'max']
