while True:    
    valor_original = float(input("Valor da compra: R$"))
    vip = str(input("Cliente VIP[S/N]: ")).upper()
    if valor_original >= 500:
        desconto = valor_original * 0.1
        valor_montante = valor_original - desconto
        if vip == "S":
            desconto_vip = valor_montante * 0.05
            valor_montante -= desconto_vip
            break
        else:
            valor_montante = valor_montante
            break
    elif valor_original < 500 and valor_original > 0:
        desconto = valor_original * 0.05
        valor_montante = valor_original - desconto
        if vip == "S":
            desconto_vip = valor_montante * 0.05
            valor_montante -= desconto_vip
            break
        else:
            valor_montante = valor_montante
            break
    else:
        print("\033[31mCalma ai patrão, tem algo errado\033[m")
        print("\033[33mTente novamente\033[m")
print("\n---Recibo de compra---")
print(f"Valor original: R${valor_original:.2f}".replace(".", ","))
if vip == "S":
    print(f"Desconto: R${desconto + desconto_vip:.2f}".replace(".", ","))
else:
    print(f"Desconto: R${desconto:.2f}".replace(".", ","))
print(f"Valor final: R${valor_montante:.2f}".replace(".", ","))
print("-"*len("---Recibo de compra---"))