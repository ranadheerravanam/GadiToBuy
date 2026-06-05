from django.urls import path

from .views import (
    home,
    vehicle_list,
    vehicle_detail,
    sell_vehicle,
    my_vehicles,
    edit_vehicle,
    delete_vehicle,
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
]