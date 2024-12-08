from .models import CustomUser
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role == CustomUser.ROLE.ADMIN and
            request.user.has_perm('manage_staff', 'manage_user', 'manage_payments', 'view_payments', 'managee_user', 'manage_holiday_plans',
                                  'view_flights_and_airlines', 'book_flights_and_buy_tickets', 'view_hotel_and_lodging_prices', 
                                  'view_transport_and_transport_fair', 'view_holiday_plans')
        )
    
class IsCustomer_User(BasePermission):
    def has_permission(self, request, view):
        return(
            request.user.is_authenticated and
            request.user.role == CustomUser.ROLE.CUSTOMER_SUPPORT and
            request.user.has_perm('view_payments', 'manage_user', 'manage_holiday_plans')
        )
    
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == CustomUser.ROLE.USER and
            request.user.has_perm('view_flights_and_airlines', 'book_flights_and_buy_tickets', 'view_hotel_and_lodging_prices', 
                                  'view_transport_and_transport_fair', 'view_holiday_plans')
        )