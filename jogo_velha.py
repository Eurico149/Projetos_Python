from random import randint


class Velha:
    def __init__(self):
        self.__velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.__historico_x = []
        self.__historico_o = []

    def reultado(self):
        for j in range(2):
            for i in range(len(self.__historico_o)):
                cont = 0
                for h in self.__historico_o:
                    if self.__historico_o[i][j] in h:
                        cont += 1
                    if cont == 3:
                        return True

        for j in range(2):
            for i in range(len(self.__historico_x)):
                cont = 0
                for h in self.__historico_x:
                    if self.__historico_x[i][j] in h:
                        cont += 1
                    if cont == 3:
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
        self.__historico_x.append(posicao)
        if self.reultado():
            print(self)
            self.__historico_x.clear()
            self.__historico_o.clear()
            self.__velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def jogada_o(self, posicao: str):
        coordenadas = self.posicao_valida(posicao)
        self.__velha[coordenadas[0]][coordenadas[1]] = "O"
        self.__historico_o.append(posicao)
        if self.reultado():
            print(self)
            self.__historico_x.clear()
            self.__historico_o.clear()
            self.__velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __str__(self):
        return ("   1   2   3\n" +
                f"a  {self.__velha[0][0]} | {self.__velha[0][1]} | {self.__velha[0][2]} \n" +
                f"b  {self.__velha[1][0]} | {self.__velha[1][1]} | {self.__velha[1][2]} \n" +
                f"c  {self.__velha[2][0]} | {self.__velha[2][1]} | {self.__velha[2][2]} \n")


if __name__ == "__main__":
    velha = Velha()
    while True:
        try:
            velha.jogada_x(input("X: "))
            velha.jogada_o(input("O: "))
        except Exception as err:
            print(err)
        print(velha)
