from unittest import TestCase

from iron_concentrate.models import IronConcentrate
from iron_concentrate.serializers import IronConcentrateSerializer, MiddleIronConcentrateSerializer


class StatisticModelSerializerTestCase(TestCase):
    def test_StatisticModelSerializer(self):
        stat_1 = IronConcentrate.objects.create(date='2021-11-12', views=32, clicks=100, cost=120)
        stat_2 = IronConcentrate.objects.create(date='2021-11-25', views=2, clicks=10, cost=1120)
        data = IronConcentrateSerializer([stat_1, stat_2], many=True).data
        print(data)
        expected_data = [
            {
                # "id": stat_1.id,
                # "cpc": format(stat_1.cost/stat_1.clicks, '.2f'),
                # "cpm": format(stat_1.cost/stat_1.views, '.2f'),
                "date": "2021-11-12",
                "views": 32,
                "clicks": 100,
                "cost": "120.00"
            },
            {
                # "id": stat_2.id,
                # "cpc": format(stat_2.cost / stat_2.clicks, '.2f'),
                # "cpm": format(stat_2.cost / stat_2.views, '.2f'),
                "date": "2021-11-25",
                "views": 2,
                "clicks": 10,
                "cost": "1120.00"
            },
        ]
        print(expected_data)
        print(data)
        self.assertEqual(expected_data, data)