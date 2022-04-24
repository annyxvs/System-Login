from os import system
from time import sleep
from initial import Initial
from register import Register

func = Initial()
reg = Register()


while True:
    system("cls")
    func.cabeçalho("PÁGINA INICIAL")

    func.menu()
    op = int(input("Escolha uma opção: "))

    if op == 0:
        system("cls")
        func.cabeçalho("REGISTER")
        reg.Register()

    elif op == 1:
        system("cls")
        func.cabeçalho("LOGIN")

    elif op == 2:
        system("cls")
        func.cabeçalho("BANCO DE DADOS")
        with open("usuarios", "r") as arquivo:
            for line in arquivo:
                print(line)
    else:
        system("cls")
        func.cabeçalho("SAINDO...")
        sleep(1.2)
        break

    cont = int(input("Deseja continuar: [1] - Sim [2] - Não: "))

    if cont == 1:
        continue
    else:
        system("cls")
        func.cabeçalho("SAINDO...")
        sleep(1.2)
        break
