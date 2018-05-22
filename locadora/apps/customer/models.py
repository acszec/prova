# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from apps.movie.models import Movie


class Customer(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    rented_movies = models.ManyToManyField(Movie)

    def __unicode__(self):
        return self.name