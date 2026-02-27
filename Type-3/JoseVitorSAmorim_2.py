#nome = str(input("Nome: "))
velocidade_permitida = float(input("Velocidade permitida: "))
velocidade_real = float(input("Velocidade real: "))
percentual = velocidade_real/velocidade_permitida
if velocidade_real <= velocidade_permitida:
    print("Sem multa")
elif percentual <= 20:
    print("Multa leve")
elif percentual <= 50:
    print("Multa grave")
elif percentual > 50:
    print("Multa gravissima")
else:
    print(0)
print(percentual)