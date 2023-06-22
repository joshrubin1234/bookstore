from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User

class UserAPITestCase(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {
            'username': 'a.ruiz',
            'password': '12345',
            'name': 'Ashly Ruiz',
            'email': 'a.ruiz@fiu.edu',
            'home_address': '123 FIU St, Miami, FL 33199',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
