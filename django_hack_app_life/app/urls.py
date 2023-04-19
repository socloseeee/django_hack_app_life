from django.urls import path, include
from .views import *


urlpatterns = [
    path('', ItemViewGetQuery.as_view(), name='item-get-query')
]
