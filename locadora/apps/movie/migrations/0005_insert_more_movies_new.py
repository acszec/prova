# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 03:49
from __future__ import unicode_literals

from django.db import migrations


def insert_movies(apps, schema_editor):
    Category = apps.get_model('category', 'Category')
    Movie = apps.get_model('movie', 'Movie')

    # COMEDIA
    lista_comedia = [
        'Click', 'O Auto da Compadecida', 'O Maskara', 'Até que a Sorte nos Separe',
        'Alexander', 'Loucademia de Pilícia 3', 'Esqueceram de mim 2'
    ]
    comedia = Category.objects.get(name="Comédia")
    for filme in lista_comedia:
        Movie.objects.create(name=filme, quantity=5, rented=0, category=comedia)

    # AVENTURA
    lista_aventura = [
        'O Rei Leão', 'O Império Contra Ataca', 'Divergente', 'Insurgente', 'Convergente', 'Jumanji'
    ]
    aventura = Category.objects.get(name="Aventura")
    for filme in lista_aventura:
        Movie.objects.create(name=filme, quantity=5, rented=0, category=aventura)

    # TERROR
    lista_terror = [
        'IT a Coisa', 'O Exorcista', 'O Iluminado', 'Psicose', 'Jogos Mortais', 'O Massacre da Serra Elétrica'
    ]
    terror = Category.objects.get(name="Terror")
    for filme in lista_terror:
        Movie.objects.create(name=filme, quantity=5, rented=0, category=terror)

    # POLICIAL
    lista_policial = [
        'O Poderoso Chefão', 'Os Infiltrados', 'Dia de Treinamento', 'Laranja Mecanica', 'Tropa de Elite 2', 'SWAT'
    ]
    policial = Category.objects.get(name="Policial")
    for filme in lista_policial:
        Movie.objects.create(name=filme, quantity=5, rented=0, category=policial)

    # ROMANCE
    lista_romance = [
        'Simplesmente Acontece', 'Um Dia', 'Titanic', 'Querido John', 'Uma Linda Mulher', 'O Melhor de Mim'
    ]
    romance = Category.objects.get(name="Romance")
    for filme in lista_romance:
        Movie.objects.create(name=filme, quantity=5, rented=0, category=romance)

    # SUSPENSE
    lista_suspense = [
        'O Sexto Sentido', 'Ilha do Medo', 'Os Suspeitos', 'Os Outros', 'Janela Indiscreta', 'Cisne Negro'
    ]
    suspense = Category.objects.get(name="Suspense")
    for filme in lista_suspense:
        Movie.objects.create(name=filme, quantity=5, rented=0, category=suspense)

class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_insert_more_movies'),
    ]

    operations = [
        migrations.RunPython(insert_movies)
    ]