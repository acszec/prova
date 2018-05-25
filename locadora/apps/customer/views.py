# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from apps.customer.models import Customer
from apps.movie.models import Movie

class CustomerListView(ListView):
    model = Customer
    context_object_name = "customer_list"
    template_name = "customer/customer_list.html"
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customer/customer_detail.html"
    context_object_name = "customer"

    def get_context_data(self, *args, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(*args, **kwargs)
        movies = Movie.objects.exclude(id__in=[c.id for c in self.object.rented_movies.all()])
        context["movies"] = movies.order_by('category')
        context["total_movies"] = movies.count()
        # import ipdb
        # ipdb.set_trace()
        return context

    def get_object(self):
        pk = self.kwargs["customer_id"]
        queryset = self.get_queryset()
        obj = queryset.get(id=pk)
        return obj

    def post(self, *args, **kwargs):
        request = self.request.POST.copy()
        del request['csrfmiddlewaretoken']
        self.object = self.get_object()
        for _id in request.keys():
            movie = Movie.objects.get(id=_id)
            if not self.object.rented_movies.filter(id=movie.id):
                self.object.rented_movies.add(movie)
                movie.rented +=1
            else:
                movie.rented -=1
                self.object.rented_movies.remove(movie)
            movie.save()
        self.object.save()
        return HttpResponseRedirect(reverse('customer_detail', kwargs={'customer_id': self.object.pk}))