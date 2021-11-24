from unittest import TestCase

from iron_concentrate.models import IronConcentrate
from iron_concentrate.serializers import IronConcentrateSerializer


class StatisticModelSerializerTestCase(TestCase):
    """test for IronConcentrateSerializer"""

    def test_StatisticModelSerializer(self):
        iron1 = IronConcentrate.objects.create(name='iron1',
                                               iron=34.65,
                                               silicon=34.65,
                                               aluminum=34.65,
                                               calcium=34.65,
                                               sulfur=34.65,
                                               month=5
                                               )
        iron2 = IronConcentrate.objects.create(name='iron2',
                                               iron=36.65,
                                               silicon=90.65,
                                               aluminum=100,
                                               calcium=10,
                                               sulfur=30.65,
                                               month=5
                                               )

        data = IronConcentrateSerializer([iron1, iron2], many=True).data
        expected_data = [
            {
                "name": "iron1",
                "iron": "34.65000",
                "silicon": "34.65000",
                "aluminum": "34.65000",
                "calcium": "34.65000",
                "sulfur": "34.65000",
                "month": 5
            },
            {
                "name": "iron2",
                "iron": "36.65000",
                "silicon": "90.65000",
                "aluminum": "100.00000",
                "calcium": "10.00000",
                "sulfur": "30.65000",
                "month": 5
            },
        ]
        self.assertEqual(expected_data, data)
