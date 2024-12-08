import json
import ast
import amadeus
from django.db.models import Q
from amadeus import Client, ResponseError, Location
from django.shortcuts import render
from django.contrib import messages
from .models import Flights, Airline, FlightImageFile, Booking
from .metric import Metrics
from .flights import Flight
from django.http import HttpResponse, Http404
from rest_framework import status
from .serializer import FlightSerializer, FlightImageFileSerializer, AirlineSerializer, BookingSerializer, CreateBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token
from rest_framework.permissions import IsAuthenticated, AllowAny

amadeus = amadeus.Client(
    client_id='YOUR_API_KEY',
    client_secret='YOUR_API_SECRET'
)

class FlightsView(APIView):
    def get(request, self):
        obj = Flight.objects.all()
        serializers = FlightSerializer(obj, many=True)
        origin = request.POST.get('Origin')
        destination = request.POST.get('Destination')
        departure_date = request.POST.get('Departuredate')
        return_date = request.POST.get('Returndate')


        kwargs = {'originLocationCode': origin,
                  'destinationLocationCode': destination,
                  'departureDate': departure_date,
                  'adults': 1
                  }

        kwargs_metrics = {'originIataCode': origin,
                          'destinationIataCode': destination,
                          'departureDate': departure_date
                          }
        trip_purpose = ''
        try:
            if return_date:
                kwargs['returnDate'] = return_date
                kwargs_trip_purpose = {'originLocationCode': origin,
                                       'destinationLocationCode': destination,
                                       'departureDate': departure_date,
                                       'returnDate': return_date
                                       }

                trip_purpose = get_trip_purpose(**kwargs_trip_purpose)
            else:
                kwargs_metrics['oneWay'] = 'true'

            if origin and destination and departure_date:
                flight_offers = get_flight_offers(**kwargs)
                metrics = get_flight_price_metrics(**kwargs_metrics)
                cheapest_flight = get_cheapest_flight_price(flight_offers)
                is_good_deal = ''
                if metrics is not None:
                    is_good_deal = rank_cheapest_flight(cheapest_flight, metrics['first'], metrics['third'])
                    is_cheapest_flight_out_of_range(cheapest_flight, metrics)

                return render(request, 'flight_price/results.html', {'flight_offers': flight_offers,
                                                                     'origin': origin,
                                                                     'destination': destination,
                                                                     'departure_date': departure_date,
                                                                     'return_date': return_date,
                                                                     'trip_purpose': trip_purpose,
                                                                     'metrics': metrics,
                                                                     'cheapest_flight': cheapest_flight,
                                                                     'is_good_deal': is_good_deal
                                                                    })
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.result['errors'][0]['detail'])

        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class FlightsDetailView(APIView):
    def get_by_id(self, id):
        try:
            flight = Flights.objects.get(id=id)
            serializer = FlightSerializer(flight)
            return Response(serializer.data)
        except Flights.DoesNotExist:
            raise Http404("flight not found")
        
    def get(self, request, id: str):
        flight = self.get_by_id(id)
        serializer = FlightSerializer(flight)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlightSearchView(APIView):
    def post(self, request):
        search_query = request.data.get('query', '')
        if search_query:
            search_results = Flight.objects.filter(
                 Q(origin__icontains=search_query) 
                | Q(destination__icontains=search_query)
                | Q(airline__name__icontains=search_query)
                | Q(departure_date__icontains=search_query)
            )
            search_results = search_results.order_by("id")
            serializers = Flight(search_results, many=True)
            return Response(serializers.data)
        return Response({"detail": "No search results found."}, status=status.HTTP_404_NOT_FOUND)  


def get_flight_offers(**kwargs):
    search_flights = amadeus.shopping.flight_offers_search.get(**kwargs)
    flight_offers = []
    for flight in search_flights.data:
        offer = Flight(flight).construct_flights()
        flight_offers.append(offer)
    return flight_offers

def get_flight_price_metrics(**kwargs_metrics):
    kwargs_metrics['currencyCode'] = 'USD'
    metrics = amadeus.analytics.itinerary_price_metrics.get(**kwargs_metrics)
    return Metrics(metrics.data).construct_metrics()

def get_trip_purpose(**kwargs_trip_purpose):
    trip_purpose = amadeus.travel.predictions.trip_purpose.get(**kwargs_trip_purpose).data
    return trip_purpose['result']

def get_cheapest_flight_price(flight_offers):
    return flight_offers[0]['price']

def rank_cheapest_flight(cheapest_flight_price, first_price, third_price):
    cheapest_flight_price_to_number = float(cheapest_flight_price)
    first_price_to_number = float(first_price)
    third_price_to_number = float(third_price)
    if cheapest_flight_price_to_number < first_price_to_number:
        return 'A GOOD DEAL'
    elif cheapest_flight_price_to_number > third_price_to_number:
        return 'HIGH'
    else:
        return 'TYPICAL'

def is_cheapest_flight_out_of_range(cheapest_flight_price, metrics):
    min_price = float(metrics['min'])
    max_price = float(metrics['max'])
    cheapest_flight_price_to_number = float(cheapest_flight_price)
    if cheapest_flight_price_to_number < min_price:
        metrics['min'] = cheapest_flight_price
    elif cheapest_flight_price_to_number > max_price:
        metrics['max'] = cheapest_flight_price

def origin_airport_search(request):
    if request.is_ajax():
        try:
            data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                        subType=Location.ANY).data
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.result['errors'][0]['detail'])
    return HttpResponse(get_city_airport_list(data), 'application/json')

def destination_airport_search(request):
    if request.is_ajax():
        try:
            data = amadeus.reference_data.locations.get(keyword=request.GET.get('term', None),
                                                        subType=Location.ANY).data
        except ResponseError as error:
            messages.add_message(request, messages.ERROR, error.response.result['errors'][0]['detail'])
    return HttpResponse(get_city_airport_list(data), 'application/json')


def get_city_airport_list(data):
    result = []
    for i, val in enumerate(data):
        result.append(data[i]['iataCode'] + ', ' + data[i]['name'])
    result = list(dict.fromkeys(result))
    return json.dumps(result)


class AirlineView(APIView):
    def get(self, request):
        obj = Airline.objects.all()
        serializers = AirlineSerializer(obj, many=True)
        return Response(serializers.errors, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = AirlineSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FlightImageFileView(APIView):
    def get(self, request):
        obj = FlightImageFile.objects.all()
        serializers = FlightImageFileSerializer(obj, many=True)
        return Response(serializers.errors, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = FlightImageFileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookingView(APIView):
    def get(self, request):
        obj = Booking.objects.all()
        serializers = BookingSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializers = CreateBookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        book = self.get_by_id(pk)
        serializers = CreateBookSerializer(book, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = self.get_by_id(pk)
        book.delete()
        return Response({"message": "Booking deleted successfully"},status=status.HTTP_200_OK)





