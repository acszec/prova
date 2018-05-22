# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from random import randint
from datetime import date

from pessoa_marked import PessoaMarkedForDeath


def criar_pessoas(quantity=151):
    for i in range(1, quantity):
        ano = str(randint(1900, 2000))
        mes = str(randint(1, 12))
        dia = str(randint(1, 28))
        pm = PessoaMarkedForDeath("{}/{}/{}".format(ano, mes, dia))
        pm.nome = "nome {}".format(i)
        yield pm

def id_autoincrement(quantity=151):
    for i in range(1, quantity):
        yield i

def matriz():
    """:return DataFrame"""
    d = {
            'id': [_id for _id in id_autoincrement(151)],
            'idade_maxima': np.random.randint(128, size=150),
            'idade_atual': np.random.randint(128, size=150),
            'classe_da_pessoa': [pessoa for pessoa in criar_pessoas(151)]
        }

    df = pd.DataFrame(data=d)
    return df

def adiciona_15aniversarios():
    """:return DataFrame com campo a mais de 15 aniversarios"""
    df = matriz()
    df["idade+15"] = df["idade_atual"].apply(lambda x: x + 15)
    return df

def adiciona_status_vida():
    """:return DataFrame com campo de status de vida da pessoa"""
    df = adiciona_15aniversarios()
    df["status_vida"] = df["classe_da_pessoa"].apply(lambda x: x.status)
    return df

def calcula_data_nascimento():
    """:return DataFrame com ano de nacimento de cada pessoa"""
    df = adiciona_status_vida()
    ano_atual = date.today().year
    df["ano_nascimento"] = df["idade_atual"].apply(lambda x: ano_atual - x)
    return df

def calcula_media():
    df = matriz()
    media = df["idade_atual"].mean()
    print media


def cria_excel():
    df = calcula_data_nascimento()
    df["classe_da_pessoa"] = df["classe_da_pessoa"].apply(lambda x: x.nome)
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print "excel criado"


print calcula_media()