from time import sleep
import JoaoLucca;

nomes = []
notas = []

class Sistema:
    def adicionar_Aluno(nome, nota):
        nomes.append(nome)
        notas.append(nota)


    def listar_Alunos():
        for i in range(len(nomes)):
            print(f"{i+1}° Aluno\nNome: {nomes[i]}\nNotas: {notas[i]}\n\n")
        print("Todos os alunos listados com sucesso! 👍")


    def alterar_Aluno(indice, nome, nota):
        nomes[indice-1] = nome
        notas[indice-1] = nota


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
            print(""" Cadastro de aluno
            [ 1 ] Adicionar aluno e notas
            [ 2 ] Listar aluno e nota
            [ 3 ] Alterar aluno e nota
            [ 4 ] Excluir aluno e nota
            [ 5 ] Sair
            """)
            option = int(input("Digite a opção desejada:"))
            print(f"Opção escolhida [ {option} ]")
            match option:
                case 1:
                    nome_aluno = input("Digite o nome do aluno: ")
                    nota_aluno = float(input("Digite a nota do aluno: "))
                    Sistema.adicionar_Aluno(nome_aluno, nota_aluno)

                case 2:
                    Sistema.listar_Alunos()
                case 3:
                    indice = -1
                    while indice < 0 or indice > len(nomes):
                        indice = int(input("Digite o indice do aluno: "))
                    nome_aluno = input("Digite o nome do aluno: ")
                    nota_aluno = float(input("Digite a nota do aluno: "))
                    Sistema.alterar_Aluno(indice, nome_aluno, nota_aluno)
                case 4:
                    Sistema.listar_Alunos()
                    indice_Aluno = int(input("Informe o indice do aluno a ser excluido: "))
                    Sistema.excluir_Aluno(indice_Aluno)
                case 5:
                    print("Saindo do sistema...")
                    sleep(2)

                case _:
                    print("Digite uma opção válida!!!")



Sistema.menu()