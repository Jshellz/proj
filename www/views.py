from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import House, Cities

# Create your views here.


def index(request):
    latest_house_list = House.objects.order_by('-pub_date')[:5]
    context = {'latest_house_list': latest_house_list}
    return render(request, 'www/index.html', context)


def detail(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    return render(request, 'www/detail.html', {'house': house})


def results(request, house_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % house_id)


def vote(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    try:
        selected_cities = house.cities_set.get(pk=request.POST['cities'])
    except (KeyError, Cities.DoesNotExist):
        return render(request, 'www/detail.html', {
            'house': house,
            'error_message': "You didn't select house",
        })
    else:
        selected_cities.cities += 1
        selected_cities.save()
        return HttpResponseRedirect(reverse('www:results', args=(house_id,)))
