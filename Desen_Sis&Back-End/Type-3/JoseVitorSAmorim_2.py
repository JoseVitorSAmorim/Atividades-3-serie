from time import sleep
while True:
    nome = str(input("Nome: "))
    velocidade_permitida = float(input("Velocidade permitida: "))
    velocidade_real = float(input("Velocidade real: "))
    if velocidade_permitida > 0 and velocidade_real > 0:
        percentual = (velocidade_real - velocidade_permitida) / velocidade_permitida * 100
        if velocidade_real <= velocidade_permitida:
            print(f"{nome} não receberá multa")
        elif percentual <= 20:
            print(f"{nome} receberá multa leve")
        elif percentual <= 50:
            print(f"{nome} receberá multa grave")
        elif percentual > 50:
            print(f"{nome} receberá multa gravissima")
    else:
        print("\033[31mCalma ai patrão, tem algo errado\033[m")
        print("\033[33mTente novamente\033[m")
        print('-' * 30)
    opcao = str(input("Deseja continuar[S/N]: ")).upper()
    if opcao == "N":
        break
    else:
        continue
print("\033[33mFinalizando o programa...\033[m")
sleep(2)
print("\033[32mObrigado por usar nosso sistema\033[m")