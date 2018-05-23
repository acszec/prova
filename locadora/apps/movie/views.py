# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic import ListView
from apps.movie.models import Movie

class MovieListView(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "movie/movie_list.html"
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(MovieListView, self).get_context_data(*args, **kwargs)
        return context
