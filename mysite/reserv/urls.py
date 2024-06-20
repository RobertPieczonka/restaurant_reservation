from django.urls import path
from .views import register, login_, logout_, homepage, restaurant_menu, reservation_user, reserve_table, check_availability

urlpatterns = [
    #rejestracja i logowanie:
    path("register", register, name="register"),
    path("login", login_, name="login_"),
    path("logout", logout_, name="logout_"),
    path('', homepage, name='homepage'),
    path('menu', restaurant_menu, name='restaurant_menu'),
    path('reserve/', reserve_table, name='reserve_table'),
    path('my_reservation/', reservation_user, name='reservation_user'),
    path('check_availability/', check_availability, name='check_availability'),

]
