# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 03:19
from __future__ import unicode_literals

from django.db import migrations

def insert_customers(apps, schema_editor):
    Customer = apps.get_model('customer', 'Customer')
    customers = [
        'Abrilina Décima Nona', 'Acheropita Papazone', 'Ácido Acético Etílico Da Silva', 'Agrícola Beterraba Areia Leão',
        'Amável Pinto', 'Amin Amou Amado', 'Antônio Treze de Junho', 'Antônio Veado Prematuro', 'Barrigudinha Seleida',
        'Bizarro Assada', 'Céu Azul do Sol Poente', 'Chevrolet da Silva Ford', 'Deust É Infinitamente', 'Faraó do Egito Souza',
        'Fernando Coelho do Rêgo', 'Himeneu Casamenteiro das Dores Conjugais', 'Jacinto Leite Aquino Rego',
        'Janeiro Fevereiro de Março Abril', 'José Casou de Calças Curtas', 'Liberdade Igualdade Fraternidade', 'Manoel Sovaco de Gambar',
        'Manuelina Terebentina Capitulina', 'Márciano Verdinho das Antenas Longas', 'Otávio Bundasseca', 'Padre Filho do Espírito Santo Amém',
        'Pália Pélia Pólia Púlia dos Guimarães', 'Paulo Jacinto Leite', 'Primavera Verão Outono Inverno',
        'Restos Mortais de Catarina', 'Rolando Escadabaixo'
    ]
    for customer in customers:
        Customer.objects.create(name=customer, is_active=True)


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_rented_movies'),
    ]

    operations = [
        migrations.RunPython(insert_customers)
    ]
