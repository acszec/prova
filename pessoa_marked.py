# -*- coding: utf-8 -*-

from pessoa import Pessoa


class PessoaMarkedForDeath(Pessoa):

    @property
    def idade_maxima(self):
        return 90

    def esta_viva(self):
        if self.idade_maxima <= self.calcula_idade():
            return False
        return True

    def faz_aniversario(self):
        if not self.esta_viva():
            return "morreu"

pm = PessoaMarkedForDeath("1890/09/30")
print pm.idade_maxima
print 'vivo', pm.esta_viva()