from django.conf.urls import re_path
from .views import *

urlpatterns = [
    # re_path(r'^makes/$', MakeListViewSet.as_view(), name='car_list'),
    re_path(r'^cars/$', CarViewSet.as_view(), name='car-list'),
    re_path(r'^rate/$', CarRateViewSet.as_view(), name='car-rate'),
    re_path(r'^cars/(?P<pk>[^/.]+)/$', CarDeleteViewSet.as_view(), name='car-delete'),
    re_path(r'^popular/$', PopularCarListViewSet.as_view(), name='popular-car-list'),
]
