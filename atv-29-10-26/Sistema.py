from time import sleep
import JoaoLucca

alunos = []

class Sistema:
    #
    #
    # Adicionei as verificações de cada função dentro delas para não sobrecarregar a função menu()
    #
    #
    def continuar():
        primeira_vez = True
        escolha = 'N'
        while escolha not in ["S", "N"]:
            if not primeira_vez: print("Digite um valor válido!!!")
            escolha = input("Você deseja continuar? [S/N]")
            escolha = escolha.upper()
            primeira_vez = False
        if escolha == "N": Sistema.menu()
        
    def adicionar_Aluno(): 
        
        nome_aluno = Sistema.digitar_nome()
        for 1 in 5:
            nota_aluno = Sistema.digitar_nota()
        alunos[-1].append([nome_aluno, [nota_aluno]])
        


    def listar_Alunos():
        
        if(len(alunos) == 0): print("Não há nenhum aluno na cadastrado.")
        
        else:
            for i in range(len(alunos)):
                for j in range(len(alunos)):
                    print(f"{i+1}° Aluno\nNome: {alunos[i]}\nNotas: {alunos[j]}\n\n")
            print("Todos os alunos listados com sucesso! 👍")


    def alterar_NomeAluno():
        #
        # A função alterar será divida em alterar nome e alterar nota do aluno, ja que estamos trabalhando com listas encadeadas
        # 
        # 

        
        #Verifica se há alunos cadastrados antes de alterar
        if len(alunos) == 0:
            print("Não há nenhum aluno na cadastrado.")
            
        else:
            indice = -1
            
            #Faz a verificação para ver se o usuário digitou o nome pela primeira vez
            primeira_vez = False
            continuar = True
            
            # Inputs
            while indice < 1 or indice > len(alunos):
                
                # Verifica se o usuário digitou o nome pela primeira vez
                if primeira_vez: 
                    print("Digite um nome válido!")
                    Sistema.continuar()
                
                indice = int(input("Digite o indice do aluno: "))
                primeira_vez = True
                
            nome_aluno = Sistema.digitar_nome()
            Sistema.continuar()
            # Inserts
            alunos[indice-1] = nome_aluno
            print("NOME DOS ALUNOS ALTERADOS")

    def excluir_Aluno(indice):
        Sistema.continuar()
        alunos.pop(indice-1) # apaga a lista do aluno todo junto com as notas

    def digitar_nome():
        #Define se o usuário está digitando pela primeira vez o nome
        primeira_vez = False
        
        #Variável para validação
        nome_invalido = True
        
        escolha = "p"
        while nome_invalido:
            
            #Essa linha só rodará ao final do while (quando o primeira vez se tornar verdadeiro)
            if primeira_vez: print("Digite um nome válido!!!")
            
            nome_aluno = input("Digite o nome do aluno: ")
            try:
                nome_invalido = nome_aluno.strip() == ""
                if not nome_invalido:
                    print(f"O nome que você digitou foi: {nome_aluno}")
                    while escolha not in ["S", "N"]:
                        escolha = input("Tem certeza da sua escolha? [S/N]")
                        escolha = escolha.upper()
                primeira_vez = True
            except ValueError:
                print(ValueError.args)
            return nome_aluno
        
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
                    if indice_Aluno < 1 or indice_Aluno > len(nomes):
                        print("Digite um índice válido!")
                    else:
                        Sistema.excluir_Aluno(indice_Aluno)
                case 5:
                    print("Saindo do sistema...")
                    sleep(2)

Sistema.menu()