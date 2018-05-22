# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from pessoa_marked import PessoaMarkedForDeath


def criar_pessoas(quantity=151):
    for i in range(1, quantity):
        pm = PessoaMarkedForDeath("1990/07/28")
        yield pm

def id_autoincrement(quantity=151):
    for i in range(1, quantity):
        yield i


d = {
        'id': [_id for _id in id_autoincrement(151)],
        'idade_maxima': np.random.randint(128, size=150),
        'idade_atual': np.random.randint(128, size=150),
        'classe_da_pessoa': [pessoa for pessoa in criar_pessoas(151)]
    }

df = pd.DataFrame(data=d)
print df