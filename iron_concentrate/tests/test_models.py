from django.test import TestCase

from iron_concentrate.models import IronConcentrate


class IronConcentrateModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        IronConcentrate.objects.create(name='iron',
                                       iron=34.65,
                                       silicon=34.65,
                                       aluminium=34.65,
                                       calcium=34.65,
                                       sulfur=34.65,
                                       month=5
                                       )

    def test_name_max_length(self):
        iron = IronConcentrate.objects.get(id=1)
        max_length = iron._meta.get_field('name').max_length
        self.assertEquals(max_length, 60)

    def test_object_name_is_last_name_comma_first_name(self):
        iron = IronConcentrate.objects.get(id=1)
        expected_object_name = '%s %s %s' % (iron.id, iron.name, iron.iron)
        self.assertEquals(expected_object_name, str(iron))
