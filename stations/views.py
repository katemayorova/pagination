from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    paginator = Paginator(data, 10)
    page_num = int(request.GET.get('page', '1'))
    page = paginator.get_page(page_num)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
