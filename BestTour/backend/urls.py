from django.urls import path

from backend.views import *

app_name = 'Backend'
urlpatterns = [
    path('tour/create/', TourCreateView.as_view()),
    path('tour/', TourListView.as_view()),
    path('tour/<int:pk>/', TourDetailView.as_view()),
    path('hotel/', HotelListView.as_view()),
    path('hottour/', HotTourListView.as_view()),
    path('request/', RequestView.as_view()),
    path('status/<int:pk>/', RequestDetailView.as_view()),
    path('status/create/', StatusCreateView.as_view()),
    path('status/', StatusListView.as_view()),
    path('meal/', TypeMealListView.as_view()),
    path('user/', UserList.as_view()),
    path('booked/', BookedTourList.as_view()),
    path('all/', AllBookedTour.as_view()),
    path('sold/', SoldTour.as_view()),
    path('clients/', ClientsBase.as_view()),
    path('invoice/', InvoiceListView.as_view()),

]
