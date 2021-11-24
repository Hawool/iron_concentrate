from rest_framework import serializers

from iron_concentrate.models import IronConcentrate


class IronConcentrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IronConcentrate
        fields = ['name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month']


class MiddleIronConcentrateSerializer(serializers.ModelSerializer):
    # middle = serializers.FloatField()
    # min = serializers.FloatField()
    # max = serializers.FloatField()

    class Meta:
        model = IronConcentrate
        fields = ['month']
