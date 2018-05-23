# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^customer/$', CustomerListView.as_view(), name='customer_list'),
    url(r'^customer/(?P<customer_id>[0-9]+)$', CustomerDetailView.as_view(), name='customer_detail'),
]