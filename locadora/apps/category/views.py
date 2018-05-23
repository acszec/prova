# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.views.generic import ListView
from apps.category.models import Category

class CategoryListView(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "category/category_list.html"
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        return context
