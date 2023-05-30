from django.shortcuts import render
from django.views import generic
from .models import Menu


# Create your views here.
class MenuList(generic.ListView):
    queryset = Menu.objects.order_by('date_created')
    template_name = 'index.html'

    def get_context_data(self):
        context = {"meals": ["Pizza", "Pasta"],
                   "ingredients": ["things"]}
        return context


class Dish(generic.DetailView):
    model = Menu
    template_name = 'dish.html'
