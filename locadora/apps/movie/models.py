# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from apps.category.models import Category


class Movie(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rented = models.IntegerField()
    category = models.ForeignKey(Category, null=True)

    def __unicode__(self):
        return self.name

    @property
    def remaining(self):
        return self.quantity - self.rented