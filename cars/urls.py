from django.conf.urls import include, re_path
from rest_framework import routers
from .views import *

#
# router = routers.DefaultRouter()
# router.register(r'', )


urlpatterns = [
    # re_path(r'', include(router.urls)),
    re_path(r'^cars/$', CarListViewSet.as_view(), name='car_list'),
    re_path(r'^cars/(?P<pk>[^/.]+)/$', CarDetailViewSet.as_view(), name='car_detail'),
]