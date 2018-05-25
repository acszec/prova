# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic import ListView, DetailView
from apps.movie.models import Movie

class MovieListView(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "movie/movie_list.html"
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super(MovieListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"
    context_object_name = "movie"

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self):
        pk = self.kwargs["movie_id"]
        queryset = self.get_queryset()
        obj = queryset.get(id=pk)
        return obj