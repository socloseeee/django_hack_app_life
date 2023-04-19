from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .serializers import MyModelSerializer
from rest_framework import views
from rest_framework.response import Response
from django.db.models.query import QuerySet


# Реализация через query-parameters
class ItemViewGetQuery(views.APIView):
    def get_queryset(self) -> QuerySet:

        inn = self.request.query_params.get('inn', None)
        nomer_zajavki = self.request.query_params.get('nomer_zajavki', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        queryset = Userdata.objects.none()
        if inn and nomer_zajavki:
            queryset = Userdata.objects.filter(inn=inn) & Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
        else:
            if inn:
                queryset = Userdata.objects.filter(inn=inn)
            elif nomer_zajavki:
                queryset = Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
        queryset = queryset.filter(date__gte=start_date, date__lte=end_date)
        queryset = queryset.order_by('-date')
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)


def pageNotFound(request, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
