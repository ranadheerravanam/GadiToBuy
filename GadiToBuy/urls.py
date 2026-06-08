from django.urls import path

from .views import (
    home,
    vehicle_list,
    vehicle_detail,
    sell_vehicle,
    my_vehicles,
    edit_vehicle,
    delete_vehicle,
    contact_seller,
    my_inquiries,
    add_favorite,
    my_favorites,
    review_seller,
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'vehicles/',
        vehicle_list,
        name='vehicle_list'
    ),

    path(
        'vehicle/<int:vehicle_id>/',
        vehicle_detail,
        name='vehicle_detail'
    ),

    path(
        'sell/',
        sell_vehicle,
        name='sell_vehicle'
    ),

    path(
        'my-vehicles/',
        my_vehicles,
        name='my_vehicles'
    ),

    path(
        'edit-vehicle/<int:vehicle_id>/',
        edit_vehicle,
        name='edit_vehicle'
    ),

    path(
        'delete-vehicle/<int:vehicle_id>/',
        delete_vehicle,
        name='delete_vehicle'
    ),

    path(
        'contact-seller/<int:vehicle_id>/',
        contact_seller,
        name='contact_seller'
    ),

    path(
        'my-inquiries/',
        my_inquiries,
        name='my_inquiries'
    ),
    path(
    'favorite/<int:vehicle_id>/',
    add_favorite,
    name='add_favorite'
    ),
    path(
    'my-favorites/',
    my_favorites,
    name='my_favorites'
  ),
    path(
    'review-seller/<int:seller_id>/',
    review_seller,
    name='review_seller'
    ),
]