from rest_framework import permissions, status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import *
from django.db.models import Count, Avg
from rest_framework.response import Response
from .models import Car


class CarViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
        ViewSet for inserting new car and return list of cars with avg_rating
    """
    queryset = Car.objects.annotate(avg_rating=Avg('rate')).order_by('pk')
    serializer_class = CarListSerializer

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
