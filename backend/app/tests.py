from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Userdata
from .serializers import MyModelSerializer

# initialize the APIClient app
client = APIClient()


class UserdataTest(APITestCase):
    def setUp(self) -> None:
        body = {
            'inn': 7707049388,
            'nomer_zajavki': 50252265,
            'start_date': "09.03.2023",
            'end_date=': "03.03.2023"
        }

    def test_get_query_with_inn_and_application(self):
        # get API response
        response = client.get(reverse('my-object-list', kwargs=self.body))
        # get data from db
        my_objects = Userdata.objects.filter(inn=self.body['inn']) & Userdata.objects.filter(nomer_zajavki=self.body['nomer_zajavki'])
        serializer = MyModelSerializer(my_objects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_query(self):
        # get API response
        response = client.get(reverse('my-object-detail', kwargs={'pk': self.my_object.pk}))
        # get data from db
        my_object = Userdata.objects.all()
        serializer = MyModelSerializer(my_object)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

