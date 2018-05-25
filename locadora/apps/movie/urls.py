# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^movie/$', MovieListView.as_view(), name='movie_list'),
    url(r'^movie/(?P<movie_id>[0-9]+)$', MovieDetailView.as_view(), name='movie_detail'),
]