from rest_framework.test import APITestCase, APIRequestFactory
from app.models import Userdata
from .views import ItemViewGetQuery

class TestItemViewGetQuery(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ItemViewGetQuery.as_view()
        self.userdata = Userdata.objects.create(
            date='2022-01-01', klient_field='test', inn=7707049388,
            nomer_zajavki=50252265, status='success'
        )
    def test_get_queryset(self):
        request = self.factory.get('', {
            'inn': 7707049388, 'nomer_zajavki': 50252265,
            'start_date': '2022-01-01', 'end_date': '2022-01-31'
        })
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['date'], '2022-01-01')
        self.assertEqual(response.data[0]['klient_field'], 'test')
        self.assertEqual(response.data[0]['inn'], 7707049388)
        self.assertEqual(response.data[0]['nomer_zajavki'], 50252265)
        self.assertEqual(response.data[0]['status'], 'success')

    def test_get_queryset_without_params(self):
        request = self.factory.get('')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
