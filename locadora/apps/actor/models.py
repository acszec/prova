# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
from apps.movie.models import Movie


class Actor(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie)

    def __unicode__(self):
        return self.name