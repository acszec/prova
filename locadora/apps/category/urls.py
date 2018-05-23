# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^category/$', CategoryListView.as_view(), name='category_list'),
]