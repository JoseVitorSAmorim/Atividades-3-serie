def linhas():
    print("-" * len("Calculadora de IRPF 2026"))

def traco():
    print("~" * len("Calculadora de IRPF 2026"))

def IRPF2026(salario_bruto):
    linhas()
    desconto_simples = 607.20

    if salario_bruto <= 1500:
        inss = salario_bruto * 0.075
    elif salario_bruto <= 2800:
        inss = salario_bruto * 0.09
    elif salario_bruto <= 4000:
        inss = salario_bruto * 0.12
    else:
        inss = 929.59

    base_calculo = salario_bruto - desconto_simples

    if base_calculo <= 2428.80:
        aliquota = 0
        parcela_deduzir = 0
    elif base_calculo <= 2826.65:
        aliquota = 0.075
        parcela_deduzir = 182.16
    elif base_calculo <= 3751.05:
        aliquota = 0.15
        parcela_deduzir = 394.16
    elif base_calculo <= 4664.68:
        aliquota = 0.225
        parcela_deduzir = 675.49
    else:
        aliquota = 0.275
        parcela_deduzir = 988.73

    imposto_base = base_calculo * aliquota - parcela_deduzir

    if salario_bruto <= 5000:
        redutor_especial = imposto_base
    elif salario_bruto > 5000 and salario_bruto <= 7350:
        redutor_especial = 978.62 - (0.133145 * salario_bruto)
    else:
        redutor_especial = 0
    imposto_final = max(0, imposto_base - redutor_especial)
    salario_liquido = salario_bruto - inss - imposto_final
    return{
        "Salário Bruto": salario_bruto,
        "INSS": inss,
        "Base de Cálculo": base_calculo,
        "Alíquota": aliquota,
        "Parcela a Deduzir": parcela_deduzir,
        "Imposto Base": imposto_base,
        "Redutor Especial": redutor_especial,
        "Imposto Final": imposto_final,
        "Salário Líquido": salario_liquido
    }
traco()
print("Calculadora de IRPF 2026")
traco()
salario = float(input("Digite o salário bruto: "))
resultado = IRPF2026(salario)
for chave, valor in resultado.items():
    print(f"{chave}: R${valor:.2f}")
print("-" * len("Calculadora de IRPF 2026"))