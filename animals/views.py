from django.core import serializers
from django.http import HttpResponse
from .models import Animal
from collections.abc import Iterable
# Create your views here.


def serialize_data(queryset):
    if isinstance(queryset, Iterable):
        return serializers.serialize('json', queryset)
    else:
        return serializers.serialize('json', [ queryset ])


def index(request):
    return HttpResponse('hello')


#the following 4 functions are for CRUD


def read_animals_data(request, animal_id=None):
    if animal_id:
        return get_animal(request, animal_id)
    animals = Animal.objects.all()
    return HttpResponse(serialize_data(animals))


def create_animal(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    breed = request.GET.get('breed')
    kind = request.GET.get('kind')
    description = request.GET.get('description')
    image_url = request.GET.get('image_url')

    try:
        animal = Animal(name=name, age=age, breed=breed, kind=kind, description=description, image_url=image_url)
        animal.save()
        return HttpResponse('Created successfully')

    except:
        return HttpResponse('Not created')

    #/create/?name=TestAnimal&age=12&breed=Yorkie&kind=D&description='My test animal'&image_url=https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12222717/Yorkshire-Terrier-Care.jpg


def update_animal(request):
    id = request.GET.get('id')
    name = request.GET.get('name')

    animal = Animal.objects.get(pk=id)

    if animal:
        animal.name = name
        animal.save()
        return HttpResponse('updated')
    else:
        return HttpResponse('no such animal')

    #/edit/?id=6&name=ChangedTestAnimalName


def delete_animal(reqquest, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
        animal.delete()
        return HttpResponse('deleted')
    except Animal.DoesNotExist:
        return HttpResponse('not deleted')

    #/delete/6



def all_dogs(request):
    dogs = Animal.objects.filter(kind='D')
    return HttpResponse(serialize_data(dogs))


def all_cats(request):
    cats = Animal.objects.filter(kind='C')
    return HttpResponse(serialize_data(cats))


def get_animal(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
        return HttpResponse(serialize_data(animal))
    except:
        return HttpResponse(None)


def search(request):
    name = request.GET.get('name')

    animals = Animal.objects.filter(name__iexact=name)
    print(animals)
    return HttpResponse(serialize_data(animals))


def owner_animals(request, owner_id):
    animals = Animal.objects.filter(owner=owner_id)
    return HttpResponse(serialize_data(animals))
