import rest_framework.exceptions
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .serializers import MyModelSerializer
from rest_framework import views
from rest_framework.response import Response
from django.db.models.query import QuerySet
from django.db.models import Count

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



# Реализация через query-parameters
class ItemViewGetQuery(views.APIView):
    """Output of the list of applications by INN/Application."""
    def get_queryset(self) -> QuerySet:

        inn = self.request.query_params.get('inn', None)
        nomer_zajavki = self.request.query_params.get('nomer_zajavki', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        queryset = Userdata.objects.values(
            'date', 'klient_field', 'inn', 'nomer_zajavki', 'status'
        ).annotate(num=Count('id')).filter(num=1)
        if self.request.query_params:
            if inn and nomer_zajavki:
                queryset = queryset.filter(inn=inn) & queryset.filter(nomer_zajavki=nomer_zajavki)
            else:
                if inn:
                    queryset = queryset.filter(inn=inn)
                elif nomer_zajavki:
                    queryset = queryset.filter(nomer_zajavki=nomer_zajavki)
            queryset = queryset.filter(date__gte=start_date, date__lte=end_date)
            queryset = queryset.order_by('-date')
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('inn', openapi.IN_QUERY, description="INN of client to be fetched (E.g.: 7707049388)",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('nomer_zajavki', openapi.IN_QUERY, description="Application number of client to be fetched (E.g.: 50252265)",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Start_date of client application to be fetched (E.g.: 09.03.2023)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="End_date of client application to be fetched (E.g.: 13.03.2023)",
                              type=openapi.TYPE_STRING),
        ],
        responses={
            200: openapi.Response(
                description='Successful response',
                schema=MyModelSerializer,
                examples={
                    'application/json': {
                        'date': '09.03.23',
                        'inn': 7707049388,
                        'nomer_zajavki': 50252265,
                        'start_date': '09.03.23',
                        'end_date': '13.03.23',
                    }
                },
            ),
            400: openapi.Response(description='Bad Request'),
        },
    )
    def get(self, request):
        queryset = self.get_queryset()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)


def pageNotFound(request, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
