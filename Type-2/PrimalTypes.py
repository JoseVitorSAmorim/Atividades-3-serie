nome=str(input("Qual seu nome completo? "))
idade=int(input"Quantos anos tens? ")
ano=int(input"Que ano nasceu? ")
cidade=str(input("Que cidade mora? "))
dist=89.6
altura=float(input("Qual sua altura? "))
salario=float(input("Quanto ganha? "))
while True:
    matricula=str(input("É matriculado[S/N]? "))
    if matricula in "Ss":
        break
    elif matricula in "Nn":
        break
    else:
        print("Erro! Tente novamente")
print(matricula)
