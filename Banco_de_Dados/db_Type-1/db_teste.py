from componentes.interface import *
from componentes.db import *
from time import sleep

criar_db()
while True:
    titulo("Bem-vindo ao GreenQuest!")
    menu(["Registrar Atividade Sustentável", "Listar Atividades Registradas", "Sair"])
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        descricao_acao = input("Descreva a atividade sustentável que realizou: ")
        pontos = int(input("Quantos pontos essa atividade vale? "))
        inserir_atividade(descricao_acao, pontos)
        print("Atividade registrada com sucesso!")
    elif escolha == '2':
        while True:
            atividades = listar_atividades()
            if atividades:
                for id, descricao_acao, pontos, data_realizacao in atividades:
                    print(f'ID: {id} | Descrição: {descricao_acao} | Pontos: {pontos} | Data: {data_realizacao}')
            else:
                print("\033[31mNenhuma atividade registrada ainda.\033[0m")
            submenu(["Sair", "Remover"])
            escolha_submenu = int(input("Escolha uma opção: "))
            if escolha_submenu == 1:
                break
            elif escolha_submenu == 2:
                id_del = int(input("Qual ID a ser apagado? "))
                if deletar(id_del):
                    print("\033[32mID excluído com sucesso!\033[0m")
                else:
                    print("\033[31mID não encontrado!\033[0m")
                linhas()
                
            else:
                print("\033[31mOpção inválida. Por favor, tente novamente.\033[0m")
    elif escolha == '3':
        print("\033[33mFinalizando o programa...\033[0m")
        sleep(2)
        break
    else:
        print("\033[31mOpção inválida. Por favor, tente novamente.\033[0m")
print("\033[32mObrigado por usar o GreenQuest! Continue praticando atividades sustentáveis!\033[0m")