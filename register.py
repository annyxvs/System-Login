import email
from os import system


class Register:
    def Register(self):
        name = str(input("Qual seu nome: "))
        email = str(input("Qual seu email: "))
        password = str(input("Qual sua senha: "))

        if (len(name) and len(email) and len(password)) == 0:
            print("Cadastro Invalido, Preencha todos os campos!!")
        elif password == email or password == name:
            print("Sua senha deve ser diferente do seu nome ou do seu email!!")
        elif (len(name) and len(email) and len(password)) != 0:
            print("Registro concluido com sucesso!!")

            usuarios = []

            usuarios.append(f"{email,password}")

            with open("usuarios", "a") as arquivo:
                for usuario in usuarios:
                    arquivo.write(f"email: {email} senha: {password}\n")
