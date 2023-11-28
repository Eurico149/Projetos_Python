from random import randint


class Velha:
    def __init__(self):
        self.__velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def reultado(self):
        for i in range(3):
            if self.__velha[i][0] == self.__velha[i][1] == self.__velha[i][2] != ' ':
                return True
            if self.__velha[0][i] == self.__velha[1][i] == self.__velha[2][i] != ' ':
                return True

        if self.__velha[0][0] == self.__velha[1][1] == self.__velha[2][2] != ' ':
            return True
        if self.__velha[0][2] == self.__velha[1][1] == self.__velha[2][0] != ' ':
            return True
        return False

    def coo_alfabetica(self, letra):
        match (letra.lower()):
            case "a":
                letra = 0
            case "b":
                letra = 1
            case "c":
                letra = 2
            case _:
                raise ValueError("Coordenada Alfabetica Invalida!")
        return letra

    def posicao_valida(self, posicao: str):
        if len(posicao) != 2:
            raise ValueError("Cordenada Invalida!")

        if posicao[0].isalpha() and posicao[1].isnumeric():
            aux1 = posicao[0]
            aux2 = int(posicao[1]) - 1
        elif posicao[1].isalpha() and posicao[0].isnumeric():
            aux1 = posicao[1]
            aux2 = int(posicao[0]) - 1
        else:
            raise TypeError("Cordenadas Invalidas!")

        aux1 = self.coo_alfabetica(aux1)

        if 0 > aux2 or aux2 > 2:
            raise ValueError("Cordenada Numerica Invalida!")
        if self.__velha[aux1][aux2] != " ":
            raise ValueError("Essa Coordenada Ja Contem Uma Jogada!")

        return aux1, aux2

    def moeda(self):
        if randint(0, 1) == 0:
            return "Cara!"
        else:
            return "Coroa!"

    def jogada_x(self, posicao: str):
        coordenadas = self.posicao_valida(posicao)
        self.__velha[coordenadas[0]][coordenadas[1]] = "X"

    def jogada_o(self, posicao: str):
        coordenadas = self.posicao_valida(posicao)
        self.__velha[coordenadas[0]][coordenadas[1]] = "O"

    def __str__(self):
        return ("\n   1   2   3\n" +
                f"a  {self.__velha[0][0]} | {self.__velha[0][1]} | {self.__velha[0][2]} \n" +
                f"b  {self.__velha[1][0]} | {self.__velha[1][1]} | {self.__velha[1][2]} \n" +
                f"c  {self.__velha[2][0]} | {self.__velha[2][1]} | {self.__velha[2][2]} \n")


if __name__ == "__main__":
    velha = Velha()
    print(velha)
    for _ in range(9):
        while True:
            try:
                velha.jogada_x(input("X: "))
                break
            except Exception as err:
                print(err)
        print(velha)
        if velha.reultado():
            break
        while True:
            try:
                velha.jogada_o(input("O: "))
                break
            except Exception as err:
                print(err)
        print(velha)
        if velha.reultado():
            break


