from rest_framework import serializers

from iron_concentrate.models import IronConcentrate


class IronConcentrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IronConcentrate
        fields = ['name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month']

