# -*- coding: utf-8 -*-

from datetime import date


class Pessoa(object):
    nome = None
    sexo = None
    altura = None
    peso = None

    def __init__(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def calcula_imc(self, peso=None, altura=None):
        self.peso = peso if peso else self.peso
        self.altura = altura if altura else self.altura
        imc = self.peso / (self.altura**2)
        return {'valor': imc, 'desc': 'imc'}

    def calcula_idade(self):
        data = self.data_nascimento.split("/")
        dia = int(data[-1])
        mes = int(data[1])
        ano = int(data[0])
        delta = date.today() - date(ano, mes, dia)
        idade = delta.days / 365
        return idade

    def faz_aniversario(self):
        data = self.data_nascimento.split("/")
        dia = int(data[-1])
        mes = int(data[1])
        ano = int(data[0])
        if dia == date.today().day and mes == date.today().month:
            return True
        return False