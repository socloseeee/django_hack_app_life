from django.urls import path
from .views import *


urlpatterns = [
    path('', ItemViewGetQuery.as_view(), name='item-get-query'),
]
