from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .serializers import MyModelSerializer
from rest_framework import views
from rest_framework.response import Response
from django.db.models.query import QuerySet
# from django.core.cache import cache
from django.db.models import Count
# from django.db.models.expressions import RawSQL


# Реализация через query-parameters
class ItemViewGetQuery(views.APIView):
    def get_queryset(self) -> QuerySet:

        inn = self.request.query_params.get('inn', None)
        nomer_zajavki = self.request.query_params.get('nomer_zajavki', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        queryset = Userdata.objects.values(
            'date', 'klient_field', 'inn', 'nomer_zajavki', 'status'
        ).annotate(num=Count('id')).filter(num=1)
        # cache.set('my_data', queryset, timeout=3600*24)
        # print(queryset)
        if inn and nomer_zajavki:
            queryset = queryset.filter(inn=inn) & queryset.filter(nomer_zajavki=nomer_zajavki)
        else:
            if inn:
                queryset = Userdata.objects.filter(inn=inn)
            elif nomer_zajavki:
                queryset = queryset.filter(nomer_zajavki=nomer_zajavki)
        queryset = queryset.filter(date__gte=start_date, date__lte=end_date)
        queryset = queryset.order_by('-date')
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)


def pageNotFound(request, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
