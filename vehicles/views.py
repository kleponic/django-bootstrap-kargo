from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import render, redirect
from vehicles.forms import ODVehicleForm
from vehicles.models import ODVehicle


def index(request):
    """
    Handle index page for vehicle
    """

    return render(request, 'vehicle/index.html')


def management(request):
    """
    Showing list of vehicle in management home page
    """

    # query on all vehicle records
    vehicles = ODVehicle.objects.all()

    # structured vehicle into simple dict, 
    # later on, in template, we can render it easily, ex: {{ vehicles }}
    data = {'vehicles': vehicles}

    return render(request, 'vehicle/management.html', data)


def create_vehicle(request):
    """
    Handle new vehicle creation
    """

    # Initial form and data
    data = {
        'form': ODVehicleForm(),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = ODVehicleForm(request.POST, request.FILES)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            # wrap form result into dict ODVehicle model fields structure 
            vehicle_data = {
                'name': form.cleaned_data.get('name'),
                'driver': form.cleaned_data.get('driver'),
                'number': form.cleaned_data.get('number'),
                'capacity': form.cleaned_data.get('capacity'),
                'photo': form.cleaned_data.get('photo'),
            }

            try:
                ODVehicle.objects.create(**vehicle_data)
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "A new record has been created!")

    return render(request, 'vehicle/create_vehicle.html', data)


def edit_vehicle(request, uuid=None):
    """
    Handle edit vehicle
    """
    if not uuid:
        return redirect(reverse('vehicle:management'))

    # validate given UUID match with record in database
    try:
        vehicle = ODVehicle.objects.get(uuid=uuid)
    except ODVehicle.DoesNotExist:
        messages.error(request, "Record not found!")
        return redirect(reverse('vehicle:management'))

    data = {
        'form': ODVehicleForm(instance=vehicle),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = ODVehicleForm(request.POST, instance=vehicle)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            try:
                form.save()
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "Record has been updated!")

    return render(request, 'vehicle/edit_vehicle.html', data)


def delete_vehicle(request, uuid=None):
    """
    Remove vehicle
    """
    if uuid:

        # finding given UUID to match vehicle in database
        try:
            vehicle = ODVehicle.objects.get(uuid=uuid)
        except ODVehicle.DoesNotExist:
            messages.error(request, "vehicle not found")
        else:
            # delete vehicle from database
            vehicle.delete()
            messages.success(request, 'vehicle "{}" has been deleted'.format(vehicle.name))

    return redirect(reverse('vehicle:management'))
