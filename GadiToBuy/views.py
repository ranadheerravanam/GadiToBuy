from django.shortcuts import render
from django.db.models import Q
from .models import Vehicle
from .forms import VehicleForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Vehicle
from .forms import VehicleForm
@login_required
def edit_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id,
        seller=request.user
    )

    if request.method == 'POST':

        form = VehicleForm(
            request.POST,
            request.FILES,
            instance=vehicle
        )

        if form.is_valid():
            form.save()
            return redirect('/my-vehicles/')

    else:

        form = VehicleForm(instance=vehicle)

    return render(
        request,
        'GadiToBuy/edit_vehicle.html',
        {'form': form}
    )


@login_required
def delete_vehicle(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id,
        seller=request.user
    )

    vehicle.delete()

    return redirect('/my-vehicles/')

@login_required
def sell_vehicle(request):

    if request.method == 'POST':

        form = VehicleForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            vehicle = form.save(commit=False)

            vehicle.seller = request.user

            vehicle.save()

            return redirect('/vehicles/')

    else:
        form = VehicleForm()

    return render(
        request,
        'GadiToBuy/sell_vehicle.html',
        {'form': form}
    )
def home(request):

    featured_vehicles = Vehicle.objects.all()[:3]

    return render(
        request,
        'GadiToBuy/home.html',
        {
            'featured_vehicles': featured_vehicles
        }
    )
def vehicle_list(request):

    query = request.GET.get('q')

    vehicles = Vehicle.objects.all()

    if query:
        vehicles = Vehicle.objects.filter(
            Q(title__icontains=query) |
            Q(brand__icontains=query) |
            Q(model__icontains=query)
        )

    return render(
        request,
        'GadiToBuy/vehicle_list.html',
        {
            'vehicles': vehicles,
            'query': query
        }
    )


def vehicle_detail(request, vehicle_id):

    vehicle = Vehicle.objects.get(id=vehicle_id)

    return render(
        request,
        'GadiToBuy/vehicle_detail.html',
        {
            'vehicle': vehicle
        }
    )
def sell_vehicle(request):

    if request.method == 'POST':

        form = VehicleForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.seller = request.user
            vehicle.save()

            return redirect('/vehicles/')

    else:
        form = VehicleForm()

    return render(
        request,
        'GadiToBuy/sell_vehicle.html',
        {'form': form}
    )
@login_required
def my_vehicles(request):

    vehicles = Vehicle.objects.filter(
        seller=request.user
    )

    return render(
        request,
        'GadiToBuy/my_vehicles.html',
        {
            'vehicles': vehicles
        }
    )