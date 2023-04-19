from django.urls import path, include
#
from .views import *
# from rest_framework import routers
# from . import views
#
# # router = routers.DefaultRouter()
# # router.register(r'items', views.ItemViewGetQuery.as_view(), basename='items')
#
urlpatterns = [
#     # path('', index, name='home'),
#
#     #path('', include(router.urls)),
#     #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#
#     #path('items/', ItemListView.as_view(), name='item-list'),
#
#     # Реализация через post-get
#     #path('items/', ItemViewPostGet.as_view(), name='item-post-get'),
#     # Реализация через query-parameters
    path('', ItemViewGetQuery.as_view(), name='item-get-query')
]
