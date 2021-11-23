from rest_framework import serializers

from iron_concentrate.models import IronConcentrate


class IronConcentrateSerializer(serializers.ModelSerializer):
    avg_iron = serializers.DecimalField(max_digits=10, decimal_places=5)
    max = serializers.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        model = IronConcentrate
        fields = '__all__'
