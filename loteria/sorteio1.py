import abc
import random


class Jogo(abc.ABC):

    @abc.abstractmethod
    def sorteio(self):
        pass

    @abc.abstractmethod
    def adiciona_numero(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class Loteria(Jogo):

    def __init__(self, quantidade=6):
        self.numeros = []
        if quantidade >= 6:
            self.quantidade = quantidade
        else:
            self.quantidade = 6

    def sorteio(self):
        return random.randint(1, 60)

    def adiciona_numero(self):
        while len(self.numeros) < self.quantidade:
            numero_sorteado = self.sorteio()
            if numero_sorteado not in self.numeros:
                self.numeros.append(numero_sorteado)

    def __len__(self):
        return len(self.numeros)

    def __getitem__(self, item):
        return self.numeros[item]

    def __str__(self):
        return str(self.numeros)
