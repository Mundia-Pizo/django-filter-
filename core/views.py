from django.shortcuts import render
from django.views.generic import ListView, View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Item

def get_item_category(request):
    return request.session['category']

class ItemListView(View):
    # model=Item
    # template_name='core/list.html'
    def get(self, request, *args, **kwargs):
        # items =Item.objects.filter(category='lady')
        ladies =Item.objects.filter(category='lady')[:4]
        babies =Item.objects.filter(category='baby')[:4]
        men =Item.objects.filter(category='men')[:4]
        context={
            'items':ladies,
            'babies':babies,
            'men':men
        }
        return render(request, 'core/list.html', context)

    def post(self,request, *args, **kwargs):
        category = request.POST.get('category')
        return HttpResponseRedirect(reverse('/'))











