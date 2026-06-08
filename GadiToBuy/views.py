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
from .models import Inquiry
from .forms import InquiryForm
from .models import Favorite
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
@login_required
def contact_seller(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    if request.method == 'POST':

        form = InquiryForm(request.POST)

        if form.is_valid():

            inquiry = form.save(commit=False)

            inquiry.vehicle = vehicle
            inquiry.buyer = request.user
            inquiry.seller = vehicle.seller

            inquiry.save()

            return redirect('/vehicles/')

    else:

        form = InquiryForm()

    return render(
        request,
        'GadiToBuy/contact_seller.html',
        {
            'vehicle': vehicle,
            'form': form
        }
    )
@login_required
def my_inquiries(request):

    inquiries = Inquiry.objects.filter(
        seller=request.user
    ).order_by('-created_at')

    return render(
        request,
        'GadiToBuy/my_inquiries.html',
        {
            'inquiries': inquiries
        }
    )
@login_required
def add_favorite(request, vehicle_id):

    vehicle = get_object_or_404(
        Vehicle,
        id=vehicle_id
    )

    Favorite.objects.get_or_create(
        user=request.user,
        vehicle=vehicle
    )

    return redirect(
        f'/vehicle/{vehicle_id}/'
    )
@login_required
def my_favorites(request):

    favorites = Favorite.objects.filter(
        user=request.user
    )

    return render(
        request,
        'GadiToBuy/my_favorites.html',
        {
            'favorites': favorites
        }
    )
@login_required
def remove_favorite(request, vehicle_id):

    Favorite.objects.filter(
        user=request.user,
        vehicle_id=vehicle_id
    ).delete()

    return redirect('/my-favorites/')
@login_required
def review_seller(request, seller_id):

    seller = User.objects.get(id=seller_id)

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.seller = seller
            review.buyer = request.user

            review.save()

            return redirect('home')

    else:

        form = ReviewForm()

    return render(
        request,
        'GadiToBuy/review_seller.html',
        {'form': form}
    )