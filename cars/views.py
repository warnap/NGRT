from rest_framework import viewsets, permissions, mixins, generics
from .models import Make, Car, Rate
from .serializers import CarSerializer, RateSerializer, MakeSerializer, CarListSerializer


class MakeListViewSer(mixins.ListModelMixin,
                      generics.GenericAPIView):
    """

    """
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)


class CarListViewSet(mixins.ListModelMixin,
                     generics.GenericAPIView):
    """

    """
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarDetailViewSet(mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    """

    """
    pass
