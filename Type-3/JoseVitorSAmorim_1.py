nome = str(input("Nome: "))
nota = float(input("Nota: "))
presenca = int(input("Presença(%): "))
if presenca >= 50 and nota >=80:
    print(f"Aluno {nome} aprovado")
elif presenca >=75 and nota >=60:
    print(f"Aluno {nome} aprovado")
else:
    print(f"Aluno {nome} reprovado")