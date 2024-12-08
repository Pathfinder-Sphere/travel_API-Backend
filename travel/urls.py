from django.urls import path
from .views import FlightsView, FlightsDetailView, FlightSearchView, AirlineView, FlightImageFileView, BookingView

urlpatterns = [
    path('flights/', FlightsView.as_view(), name='flight-list'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('booking/<int:pk>/', BookingView.as_view(), name='booking-detail'),
    # path('booking/cancel/<int:pk>/', BookingCancelView.as_view(), name='booking-cancel'),
    # path('booking/confirm/<int:pk>/', BookingConfirmView.as_view(), name='booking-confirm'),
    # path('booking/history/', BookingHistoryView.as_view(), name='booking-history'),
    # path('booking/payment/<int:pk>/', BookingPaymentView.as_view(), name='booking-payment'),
    # path('booking/payment/success/<int:pk>/', BookingPaymentSuccessView.as_view(), name='booking-payment-success'),
    # path('booking/payment/failure/<int:pk>/', BookingPaymentFailureView.as_view(), name='booking-payment-failure'),
    path('airline/', AirlineView.as_view(), name='airline-list'),
    # path('airline/<int:pk>/', AirlineDetailView.as_view(), name='airline-detail'),
    # path('airline_search/', AirlineSearchView.as_view(), name='airline-search'),
    path('<str:id>/', FlightsDetailView.as_view(), name='flight_details'),
    path('search/', FlightSearchView.as_view(), name='flight_search'),
    path('image/', FlightImageFileView.as_view(), name='flight_image'),

]
