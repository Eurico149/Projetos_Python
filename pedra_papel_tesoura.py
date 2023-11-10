from random import randint


def escolha(alternativa: int):
    match alternativa:
        case 1:
            return "Pedra"
        case 2:
            return "Papel"
        case 3:
            return "Tesoura"
        case _:
            raise Exception("Alternativa invalida!")


tamanho = int(input("Tamanho do Campeonato: "))
contadorv = 0
contadord = 0

print(f"MELHOR DE {tamanho}")
while contadord <= tamanho // 2 and contadorv <= tamanho // 2:
    mao = int(input("\n1. Pedra\n"
                    "2. Papel\n"
                    "3. Tesoura\n"
                    "Escolha: "))
    aux = randint(1, 3)

    if (mao == 3 and aux == 1) or (mao == 2 and aux == 3) or (mao == 1 and aux == 2):
        contadord += 1
        print(f"{escolha(mao)} VS {escolha(aux)}\nRESULTADO -> Derrota")
        print(f"{contadorv}/{contadord}")
    elif aux == mao:
        print(f"{escolha(mao)} VS {escolha(aux)}\nRESULTADO -> Empate")
    else:
        contadorv += 1
        print(f"{escolha(mao)} VS {escolha(aux)}\nRESULTADO -> Vitoria")
        print(f"{contadorv}/{contadord}")

print(f"\nRESULTADO FINAL: {contadorv}/{contadord}")
