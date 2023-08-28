import pkgutil
from typing import Any, Dict
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
import datetime
from django.urls import reverse, reverse_lazy
from django.views import View
from users.models import User
from .models import Ads, Category
from .forms import AdForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView



def category_list(request):
    all_categories = Category.objects.all()
    context = {
        "all_categories": all_categories
    }
    return render(request, 'category.html', context=context)


class AdsListView(ListView):
    template_name = 'index.html'
    queryset = Ads.objects.all()
    context_object_name = 'all_ads'
    

class AdsDetailView(DetailView):
    template_name = 'retrieve.html'
    queryset = Ads.objects.all()
    context_object_name = 'ad'

class AdsUpdateView(UpdateView):
    template_name = 'update_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads-list')
    
class AdsDeleteView(DeleteView):
    template_name = 'delete_ad.html'
    queryset = Ads.objects.all()
    success_url = reverse_lazy('ads-list')

class AdsCreateView(CreateView):
    template_name = 'create_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads-list')


    # def get(self, **kwargs: Any):
    #     all_ads = Ads.objects.all()
    #     return render(request, self.template_name)

    # def get(self, request, *args, **kwargs):
    #     all_ads = Ads.objects.all()
    #     return render(request, self.template_name, {'all_ads': all_ads})

    # all_ads = Ads.objects.filter(description__contains="S ", created_at__year=2023)  #работает №4

    # all_ads = Ads.objects.filter(title__contains="test") # работает №2

    # all_ads = Ads.objects.filter(owner__exact=None) # работает №3

    # all_ads = Ads.objects.filter(price__in=[200, 3000, 343, 2500]) # работает №6

    # all_ads = Ads.objects.filter(created_at__lte=timezone.now()) #№1

    # bekbol = User.objects.get(username='bekbol') #№5
    # all_ads = Ads.objects.filter(owner=bekbol)    


    # first = all_ads[0]
    # print(type(all_ads))
    # print(first.title)
    # print(first.description)
    # print(first.price)
    # print(all_ads)
    # print(first.image.url)
    # context = {
    #     "all_ads": all_ads
    # }
    # return render(request, 'index.html', context = context)


def created_at(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ads-list')
    else:
        form_of_ad = AdForm()
    return render(request, 'create_ad.html', {'form_of_ad': form_of_ad})


def update_ad(request, pk):
    ad = get_object_or_404(Ads, id=pk)
    
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Success edited </h2>')
        else:
            return HttpResponse('<h1> Error edited </h1>')
    else:
        form_of_ad = AdForm(instance=ad)
        return render(request, 'update_ad.html', {'form_of_ad': form_of_ad})


def retrieve_ad(request, pk):
    ad = get_object_or_404(Ads, id=pk)
    # ad = Ads.objects.get(id=pk)
    context = {
        'ad': ad
    }
    return render(request, 'retrieve.html', context=context)


def delete_ad(request, pk):
    ad = Ads.objects.get(id=pk)
    ad.delete()
    messages.success(request, 'Обьект успешно удалён.')
    return redirect('ads-list')


                                           