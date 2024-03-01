import numpy as np
import random


def put_bombs(numerobombas, campo):
    lista = []
    for i in range(numerobombas):
        posicao = (random.randint(0, campo.shape[0]-1), random.randint(0, campo.shape[1]-1))
        while posicao in lista:
            posicao = (random.randint(0, campo.shape[0]-1), random.randint(0, campo.shape[1]-1))
        campo[posicao[0]][posicao[1]] = -1
        lista.append(posicao)


def quantidade_bombas(h, w, difi):
    match difi:
        case 1:
            return (h * w) // 9
        case 2:
            return (h * w) // 6
        case 3:
            return (h * w) // 4
        case 4:
            return int((h * w) / 2.5)
        case _:
            raise Exception("Dificuldade Invalida!")


def organizar_tabuleiro(campo):
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            if campo[i][j] == -1:
                aux = (-1, 0, 1)
                for w in range(3):
                    for q in range(3):
                        if 0 <= i + aux[w] < campo.shape[0] and 0 <= j + aux[q] < campo.shape[1]:
                            if campo[i + aux[w]][j + aux[q]] != -1:
                                campo[i + aux[w]][j + aux[q]] += 1


class CampoMinado:
    def __init__(self, heigth: int, width: int, dificuldade=2):
        self.__campominado = np.zeros((heigth, width), dtype=int)
        self.__bombas = quantidade_bombas(heigth, width, difi=dificuldade)
        put_bombs(self.__bombas, self.__campominado)
        organizar_tabuleiro(self.__campominado)
        self.__campoplayer = np.zeros((heigth, width), dtype=int)
        self.__jogando = True

    @property
    def jogando(self):
        return self.__jogando

    def __limpa_zero(self, x, y, posicoes: list):
        for w in range(-1, 2):
            for q in range(-1, 2):
                if 0 <= x + w < self.__campoplayer.shape[0] and 0 <= y + q < self.__campoplayer.shape[1]:
                    if (x + w, y + q) not in posicoes:
                        posicoes.append((x + w, y + q))
                        if self.__campominado[x + w][y + q] > 0:
                            self.__campoplayer[x + w][y + q] = self.__campominado[x + w][y + q]
                        elif self.__campominado[x + w][y + q] == 0:
                            self.__limpa_zero(x + w, y + q, posicoes)

    def selecionar(self, x: int, y: int):
        local = self.__campominado[x][y]
        if local == 0:
            posicoes = [(x, y)]
            self.__limpa_zero(x, y, posicoes)
        elif local == -1:
            self.__campoplayer[x][y] = -1
            self.__jogando = False
        else:
            self.__campoplayer[x][y] = local

    def getcampo(self):
        return self.__campominado

    def __str__(self):
        return str(self.__campoplayer)


if __name__ == "__main__":
    campominaro = CampoMinado(10, 12, dificuldade=2)
    while campominaro.jogando:
        print(campominaro)
        campominaro.selecionar(int(input()), int(input()))
    print(campominaro)

