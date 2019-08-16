# -- coding: utf-8 --
import time
import os
import IP2Location
import re

clear = lambda: os.system("cls")
check = False
conteudo = ""
achou = int = 0
adiMais = "S"
proMais = "S"
database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.BIN"))


while check == False:
    # Dando uma escolha entre 3 tarefas

    Escolha = float(input(
        "Selecione alguma das opções abaixo: \n 1- Verifição de endereço do Remetente \n 2- Verificar IP de origem \n 3- apagar um registro \n"))

    # If para achar qual tarefa o usuário quer
    if Escolha == 1:
        clear()
        print("Abrindo sistema para PROCURAR um registro...")
        time.sleep(2)
        while proMais == "S":
            clear()
            procurando = "Received: "
            with open("Registros.txt", "r") as arq:
                for linha in arq:
                    if linha.find(procurando) > -1:
                        print(linha)
                        achou += 1
            print("Tarefa concluida.\n")
            if achou <= 0:
                print("Não foi encontrado nenhum registro com esse nome ou código.\n")
            elif achou == 1:
                print("Foi encontrado", achou, " registro.\n")
            else:
                print("Foram encontrados", achou, " registros.\n")
            achou = 0
            proMais = input("Você precisa procurar mais algum registro? \n (S/N) \n").upper()

            adiMais = input("Você precisa adicionar mais algum regitro? \n (S/N) \n").upper()

    elif Escolha == 2:
        clear()
        print("Abrindo sistema para PROCURAR um registro...")
        time.sleep(2)
        while proMais == "S":
            clear()
            procurando = "IP"
            #print(procurando)
            with open("Registros.txt", "r") as arq:
                for linha in arq:
                    if linha.find(procurando) > -1:
                        #print(linha)
                        ipResult = re.findall(r'[0-9]+(?:\.[0-9]+){3}', linha)
            print("O seu IP resultante é: ", ipResult )
            achou += 1
            #rec = database.get_all(ipResult)
            print("Tarefa concluida.\n")
            if achou <= 0:
                print("Não foi encontrado nenhum registro com esse nome ou código.\n")
            elif achou == 1:
                print("Foi encontrado", achou, " registro.\n")
            else:
                print("Foram encontrados", achou, " registros.\n")
            achou = 0
            proMais = input("Você precisa procurar mais algum registro? \n (S/N) \n").upper()

    elif Escolha == 3:
        clear()
        print("Tarefa ainda não adicionada.")
        time.sleep(0)

    else:
        clear()
        Escolha = int(input(
            "Opção Inválida, Escolha corretamente:\n 1- Verifição de endereço do Remetente \n 2- Verificar IP de origem \n 3- apagar um registro \n"))
    algo = input("Precisa fazer mais alguma coisa? \n (S/N) \n").upper()



