from time import sleep
import JoaoLucca;

nomes = []
notas = []

class Sistema:
    #
    #
    # Adicionei as verificações de cada função dentro delas para não sobrecarregar a função menu()
    #
    #
    def adicionar_Aluno(): 
        nome_aluno = input("Digite o nome do aluno: ")
        # arrumar esta verificação de espaços brancos do nome
        if (nome_aluno.strip == "") or (nome_aluno.isnumeric):
            print("Digite um nome válido!!!")
            while (nome_aluno.strip == "") or (nome_aluno.isnumeric):
                nome_aluno = input("Digite o nome do aluno: ")
        nota_aluno = Sistema.digitar_nota
        nomes.append(nome_aluno)
        notas.append(nota_aluno)


    def listar_Alunos():
        for i in range(len(nomes)):
            print(f"{i+1}° Aluno\nNome: {nomes[i]}\nNotas: {notas[i]}\n\n")
        print("Todos os alunos listados com sucesso! 👍")


    def alterar_Aluno():
        indice = -1
        # Inputs
        while indice < 0 or indice > len(nomes):
            indice = int(input("Digite o indice do aluno: "))
        nome_aluno = input("Digite o nome do aluno: ")
        if (nome_aluno.strip == "") or (nome_aluno.isnumeric):
            print("Digite um nome válido!!!")
            while (nome_aluno.strip == "") or (nome_aluno.isnumeric):
                nome_aluno = input("Digite o nome do aluno: ")
        nota_aluno = Sistema.digitar_nota
        # Inserts
        nomes[indice-1] = nome_aluno
        notas[indice-1] = nota_aluno


    def excluir_Aluno(indice):
            nomes.pop(indice-1)
            notas.pop(indice-1) 


    def digitar_nota():
        nota_aluno = 0
        validacao = False
        while not validacao:
            nota_aluno = float(input("\nDigite a nota do aluno"))
            validacao = JoaoLucca.validarNota(nota_aluno)
            if not validacao:
                print("\nDigite uma nota válida 😡")
        return nota_aluno


    def menu():
        option = 0
        while option != 5:
            try:
                print(""" Cadastro de aluno
                [ 1 ] Adicionar aluno e notas
                [ 2 ] Listar aluno e nota
                [ 3 ] Alterar aluno e nota
                [ 4 ] Excluir aluno e nota
                [ 5 ] Sair
                """)
                option = int(input("Digite a opção desejada:"))
                if option < 1 or option > 5:
                    print("Dígito errado, digite corretamente uma das opções. ")
                    Sistema.menu()
                else:
                    print(f"Opção escolhida [ {option} ]")
            except ValueError:
                print("\nDigite a opção válida para o cadastro!😡😡\n")
                Sistema.menu()
            match option:
                case 1:
                    Sistema.adicionar_Aluno()
                case 2:
                    Sistema.listar_Alunos()
                case 3:
                    Sistema.alterar_Aluno()
                case 4:
                    Sistema.listar_Alunos()
                    indice_Aluno = int(input("Informe o indice do aluno a ser excluido: "))
                    if (indice_Aluno < len(nomes) and indice_Aluno < len(notas)) or (indice_Aluno > len(nomes) and indice_Aluno > len(notas)):
                        print("Digite um indice valido!!!!")
                    Sistema.excluir_Aluno(indice_Aluno)
                case 5:
                    print("Saindo do sistema...")
                    sleep(2)

Sistema.menu()