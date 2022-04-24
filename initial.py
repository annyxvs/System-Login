from os import system


class Initial:
    def cabeçalho(self, title):
        print("=" * 30)
        print(f"        {title}")
        print("=" * 30)

    def menu(self):
        names = ["Register", "Login", "Banco de Dados", "Sair"]
        cont = 0
        while cont <= 3:
            for name in names:
                print(f"[{cont}] - {name}")
                cont = cont + 1
        
       