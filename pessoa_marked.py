# -*- coding: utf-8 -*-

from pessoa import Pessoa


class PessoaMarkedForDeath(Pessoa):

    status = "viva"

    @property
    def idade_maxima(self):
        return 85

    @property
    def status(self):
        status = "viva" if self.faz_aniversario() else "morta"
        return status

    def esta_viva(self):
        if self.idade_maxima <= self.calcula_idade():
            return False
        return True

    def faz_aniversario(self):
        if not self.esta_viva():
            return False
        return True