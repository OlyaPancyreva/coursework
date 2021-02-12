from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# CREATE
class TourCreateView(generics.CreateAPIView):
    serializer_class = TourCreateSerializer


class StatusCreateView(generics.CreateAPIView):
    serializer_class = StatusSerializer


# GET всех
class TourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()


class InvoiceListView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


class HotelListView(APIView):
    def get(self, request):
        hotel = Hotel.objects.all()
        serializer = HotelSerializer(hotel, many=True)
        return Response(serializer.data)


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class BookedTourList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        booked = BookedTour.objects.all()
        serializer = BookedTourSerializer(booked, many=True)
        return Response(serializer.data)

    def post(self, request):
        tour = BookedTourPostSerializer(data=request.data)
        if tour.is_valid():
            tour.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class SoldTour(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        booked = BookedTour.objects.filter(status__in=[6, 7])
        serializer = BookedTourSerializer(booked, many=True)
        return Response(serializer.data)


class AllBookedTour(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        booked = BookedTour.objects.all()
        serializer = BookedTourSerializer(booked, many=True)
        return Response(serializer.data)


class ClientsBase(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        booked = BookedTour.objects.all().distinct('user')
        serializer = BookedTourSerializer(booked, many=True)
        return Response(serializer.data)


class HotTourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    queryset = Tour.objects.filter(HotTour=True)


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class RequestView(APIView):
    def get(self, request):
        request = Request.objects.all()
        serializer = RequestSerializer(request, many=True)
        return Response(serializer.data)

    def post(self, request):
        request = RequestPostSerializer(data=request.data)
        if request.is_valid():
            request.save()
            return Response(status=201)
        else:
            return Response(status=400)


class TypeMealListView(generics.ListAPIView):
    serializer_class = TypeMealSerializer
    queryset = MealType.objects.all()


# GET, UPDATE, DELETE
class TourDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TourSerializer
    queryset = Tour.objects.all()


class RequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequestEditSerializer
    queryset = Request.objects.all()
