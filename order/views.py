from django.shortcuts import render
from django.http import HttpResponse
from toursale.models import TourSaleEnd


def get_last_order(request):
    return HttpResponse(max(map(lambda x: x.id, TourSaleEnd.objects.all())))
