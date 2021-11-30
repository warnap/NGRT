from rest_framework import viewsets, permissions, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import *
from .externalAPI import check_make, check_make_model
from django.db.models import Count, Avg
from rest_framework.response import Response
from .models import Make, Car, Rate


class MakeListViewSet(ListModelMixin,
                      GenericAPIView):
    """

    """
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)


# class CarViewSet(viewsets.ViewSet, GenericAPIView):
#     def list(self, request, *args, **kwargs):
#         queryset = Car.objects.all()
#         serialzer
#         return Response(serializer.data)
#
#     def create(self):
#         pass


class CarViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
        ViewSet for inserting new car and return list of cars with avg_rating
    """
    queryset = Car.objects.annotate(avg_rating=Avg('rate')).order_by('pk')
    serializer_class = CarListSerializer
    custom_serializer_classes = {
        'create': CarCreateSerializer,
    }
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CarDeleteViewSet(DestroyModelMixin,
                       GenericAPIView):
    """
        ViewSet only for car delete by car_id
    """
    queryset = Car.objects.all()
    permission_classes = [permissions.AllowAny]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PopularCarListViewSet(ListModelMixin,
                            GenericAPIView):
    """
        ViewSet for return list of cars with rating_number
    """
    queryset = Car.objects.annotate(rates_number=Count('rate')).order_by('pk')
    serializer_class = PopularCarListSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)


class CarRateViewSet(CreateModelMixin, GenericAPIView):
    """
        ViewSet for post rating
    """
    serializer_class = RateSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RateSerializer(
            data=request.data
        )
        if serializer.is_valid():
            return self.create(request)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
