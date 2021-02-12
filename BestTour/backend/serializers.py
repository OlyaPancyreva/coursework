from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ("name",)


class TypeMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealType
        fields = ("name",)


class HotelSerializer(serializers.ModelSerializer):
    roomType = RoomSerializer()

    class Meta:
        model = Hotel
        fields = ("name", "city", "rating", "roomType")


class TourSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    mealType = TypeMealSerializer()

    class Meta:
        model = Tour
        fields = "__all__"


class TourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("status", "id")


class RequestSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Request
        fields = '__all__'


class RequestEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("status",)


class RequestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("name", "mail", "phone")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class BookedTourSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tour = TourSerializer()
    status = StatusSerializer()

    class Meta:
        model = BookedTour
        fields = '__all__'


class BookedTourPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedTour
        fields = ("tour",)


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
