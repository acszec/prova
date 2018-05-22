# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from random import randint

from pessoa_marked import PessoaMarkedForDeath


def criar_pessoas(quantity=151):
    for i in range(1, quantity):
        ano = str(randint(1900, 2000))
        mes = str(randint(1, 12))
        dia = str(randint(1, 30))
        pm = PessoaMarkedForDeath("{}/{}/{}".format(ano, mes, dia))
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

def adiciona_15aniversarios(df):
    """:return DataFrame com campo a mais de 15 aniversarios"""
    df["idade+15"] = df["idade_atual"].apply(lambda x: x + 15)
    return df

def adiciona_status_vida(df):
    """:return DataFrame com campo de status de vida da pessoa"""
    df["status_vida"] = df["classe_da_pessoa"].apply(lambda x: x.status)
    return df

print adiciona_status_vida(adiciona_15aniversarios(matriz()))