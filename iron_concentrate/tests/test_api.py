from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class StatisticModelTestCase(APITestCase):
    """testing methods: get, post"""

    def setUp(self):
        self.data = {
            "name": "iron1",
            "iron": "34.65000",
            "silicon": "34.65000",
            "aluminum": "34.65000",
            "calcium": "34.65000",
            "sulfur": "34.65000",
            "month": 5
        }
        self.wrong_data = {
            "name": "iron1",
            "iron": "iron",
            "silicon": "34.65000",
            "aluminum": "34.65000",
            "calcium": "34.65000",
            "sulfur": "34.65000",
            "month": 5
        }
        self.user = get_user_model().objects.create_user(username='sam', password='sam')
        self.authorized_client = APIClient()
        response = self.authorized_client.post('/auth/token/login/', {'username': 'sam', 'password': 'sam'})
        self.authorized_client.force_authenticate(self.user, response.data['auth_token'])

    def test_can_create_iron_concentrate(self):
        url = '/api/v1/iron_concentrate'
        response = self.authorized_client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_iron_concentrate(self):
        url = '/api/v1/iron_concentrate'
        response = self.authorized_client.post(url, self.wrong_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_read_iron_concentrate_list(self):
        response = self.authorized_client.get('/api/v1/iron_concentrate')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_iron_concentrate_middle(self):
        url = '/api/v1/iron_concentrate/middle'
        response = self.authorized_client.post(url, {"month": 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
