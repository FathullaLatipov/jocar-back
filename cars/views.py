from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from cars.models import CarModel


class HomeView(ListView):
    template_name = 'index.html'
    queryset = CarModel.objects.all()
    context_object_name = 'lists'


class ModelsView(ListView):
    template_name = 'models.html'
    queryset = CarModel.objects.all()
    context_object_name = 'models'


class WishlistModelListView(ListView):
    template_name = 'wishlist.html'
    paginate_by = 7

    def get_queryset(self):
        return CarModel.get_from_wishlist(self.request)


def add_to_wishlist(request, pk):
    try:
        product = CarModel.objects.get(pk=pk)
    except CarModel.DoesNotExist:
        return Response(data={'status': False})
        # if not wishlist:
        #     wishlist = []
    wishlist = request.session.get('wishlist', [])
    if product.pk in wishlist:
        wishlist.remove(product.pk)
        data = {'status': True, 'added': False}
    else:
        wishlist.append(product.pk)
        data = {'status': True, 'added': True}
    request.session['wishlist'] = wishlist

    return JsonResponse(data)
