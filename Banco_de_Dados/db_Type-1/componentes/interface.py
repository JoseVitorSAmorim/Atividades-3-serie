def linhas():
    print("-" * 50)

def titulo(texto):
    linhas()
    print(f'{texto:^50}')
    linhas()

def menu(lista):
    titulo("MENU")
    submenu(lista)

def submenu(lista):
    for i, item in enumerate(lista, 1):
        print(f'\033[33m{i}\033[0m - \033[34m{item}\033[0m')
    linhas()