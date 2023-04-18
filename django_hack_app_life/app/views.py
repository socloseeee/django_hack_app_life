from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.db import connection
from .forms import *
from .models import *
from .serializers import MyModelSerializer
from rest_framework import viewsets, generics, status, views
from rest_framework.response import Response
from django.db.models.query import QuerySet
from django.db.models import Q

# Реализация через post-get
class ItemViewPostGet(views.APIView):
    def get(self, request):
        inn = request.session.get('inn')
        nomer_zajavki = request.session.get('nomer_zajavki')
        items = Userdata.objects.none()
        if inn and nomer_zajavki:
            items = Userdata.objects.filter(inn=inn) & Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
        else:
            if inn:
                items = Userdata.objects.filter(inn=inn)
            elif nomer_zajavki:
                items = Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
            else:
                return Response({"error": "No item found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MyModelSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            request.session["inn"] = serializer.data.get("inn") # в параметры сессии присваиваем данные
            request.session["nomer_zajavki"] = serializer.data.get("nomer_zajavki")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Реализация через query-parameters
class ItemViewGetQuery(generics.ListAPIView):
    serializer_class = MyModelSerializer
    template_name = 'app/index.html'
    context_object_name = 'post'
    def get_queryset(self):
        queryset = Userdata.objects.none()
        inn = self.request.query_params.get('inn', None)
        nomer_zajavki = self.request.query_params.get('nomer_zajavki', None)
        if inn and nomer_zajavki:
            queryset = Userdata.objects.filter(inn=inn) & Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
        else:
            if inn:
                queryset = Userdata.objects.filter(inn=inn)
            elif nomer_zajavki:
                queryset = Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
        return queryset

# class ItemCreateView(views.APIView):
#     def post(self, request):
#         serializer = MyModelSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def execute_db(condition) -> list:
#     with connection.cursor() as cursor:
#         cursor.execute(f"SELECT Klient, Nomer_zajavki, Status FROM Userdata Where {condition}")
#         return cursor.fetchall()



# class UserView(viewsets.ModelViewSet):
#     serializer_class = MyModelSerializer
#     template_name = 'app/index.html'
#     context_object_name = 'post'
#
#     def get_queryset(self):
#         # print(self.kwargs.get())
#         queryset = Userdata.objects.none()
#         inn = self.request.query_params.get('inn', None)
#         nomer_zajavki = self.request.query_params.get('nomer_zajavki', None)
#         if inn and nomer_zajavki:
#             queryset = Userdata.objects.filter(inn=inn) & Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
#         else:
#             if inn:
#                 queryset = Userdata.objects.filter(inn=inn)
#             elif nomer_zajavki:
#                 queryset = Userdata.objects.filter(nomer_zajavki=nomer_zajavki)
#        return queryset

# def index(request) -> HttpResponse:
#     inn_val: str = ''
#     nomer_val: str = ''
#     radio_choice: str = ''
#     application: QuerySet = Userdata.objects.none()
#     if request.method == 'POST':
#         inn: Inn = Inn(request.POST)
#         nomer: Nomer = Nomer(request.POST)
#         radio: RadioButton = RadioButton(request.POST)
#         if radio.is_valid():
#             radio_choice: QueryDict = request.POST['my_choice_field']
#             try:
#                 if radio_choice == '1' and inn.is_valid():
#                     inn_val = request.POST['inn']
#                     choice = 'inn=' + inn_val
#                     application = execute_db(choice)
#                 if radio_choice == '2' and nomer.is_valid():
#                     nomer_val = request.POST['nomer_zajavki']
#                     choice = 'Nomer_zajavki=' + nomer_val
#                     application = execute_db(choice)
#                 if radio_choice == '3' and inn.is_valid() and nomer.is_valid():
#                     inn_val = request.POST['inn']
#                     nomer_val = request.POST['nomer_zajavki']
#                     choice = 'inn=' + inn_val + ' AND ' + 'Nomer_zajavki=' + nomer_val
#                     application = execute_db(choice)
#             except ValidationError as e:
#                 nomer.add_error(e) if inn.is_valid() else inn.add_error(e)
#
#     else:
#         inn: Inn = Inn()
#         nomer: Nomer = Nomer()
#         radio: RadioButton = RadioButton()
#     context: dict = {
#         'inn_val': inn_val,
#         'nomer_val': nomer_val,
#         'radio': radio,
#         'inn': inn,
#         'nomer': nomer,
#         'title': 'TITLE',
#         'application': application
#     }
#     return render(request, 'app/index.html', context=context)


def pageNotFound(request, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
