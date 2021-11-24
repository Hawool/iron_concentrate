from django.test import TestCase

from iron_concentrate.models import IronConcentrate


class IronConcentrateModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        IronConcentrate.objects.create(name='iron',
                                       iron=34.65,
                                       silicon=34.65,
                                       aluminum=34.65,
                                       calcium=34.65,
                                       sulfur=34.65,
                                       month=5
                                       )

    def test_name_max_length(self):
        """test for max_length in name field of IronConcentrate"""
        iron = IronConcentrate.objects.get(id=1)
        max_length = iron._meta.get_field('name').max_length
        self.assertEquals(max_length, 60)

    def test_object_name(self):
        """test for object name"""
        iron = IronConcentrate.objects.get(id=1)
        expected_object_name = '%s %s %s' % (iron.id, iron.name, iron.iron)
        self.assertEquals(expected_object_name, str(iron))

    def test_decimal_params(self):
        """test for decimal params"""
        iron = IronConcentrate.objects.get(id=1)
        max_digits = iron._meta.get_field('aluminum').max_digits
        decimal_places = iron._meta.get_field('aluminum').decimal_places
        self.assertEquals(max_digits, 10)
        self.assertEquals(decimal_places, 5)
