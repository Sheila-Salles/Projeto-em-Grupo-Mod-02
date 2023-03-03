import csv
import datetime
hora_atual = datetime.datetime.now()
print(hora_atual)

print("\n     Criar aquivo CSV\n")
#a=(input("Digite o nome do arquivo: "))
arquivo = open("./Arquivo.csv", "w", newline="", encoding="utf-8")
adicionar = csv.writer(arquivo)
resultado = []
    # 3. grava as linhas
for cont in range(0,1,1):
    adicionar.writerow(["Idade", "Gênero", "Pergunta_1", "Pergunta_2", "Pergunta_3", "Pergunta_4"])        
def entrevista():
    import csv
    from time import sleep
    import datetime
    hora_atual = datetime.datetime.now()
    print(hora_atual)

    print("\n     Criar aquivo CSV\n")
    #a=(input("Digite o nome do arquivo: "))
    arquivo = open("./Arquivo.csv", "a", newline="", encoding="utf-8")
    
    # 2. cria o objeto de gravação
    adicionar = csv.writer(arquivo)
    
    # 3. grava as linhas
    for cont in range(0,1,1):
        adicionar.writerow(["Idade", "Gênero", "Pergunta_1", "Pergunta_2", "Pergunta_3", "Pergunta_4"])        
        opcao = 0
        while opcao !="00":
            try:           
                resultado.append(int(input("Digite a idade: ")))
                if(opcao==00):
                    print("\n""Aplicativo encerrado.\n")
                    exit
            except:
                print("Tente novamente")
                break
            try:
                resultado.append(input("Digite a Gênero: "))
            except:
                print("Tente novamente")
                continue                
            try:
                opcao = int(input("Você costuma ouvir música por estações de rádio: \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            except:
                print("Tente novamente")
                continue
            if (opcao==1):
                resultado.append("Sim")
            elif(opcao==2):
                resultado.append("Não")
            elif(opcao==3):
                resultado.append("Poucas vezes")
            elif(opcao==4):
                break
            try:
                opcao = int(input("Você reserva um tempo do seu dia para ouvir suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            except:
                print("Tente novamente")
                continue
            if (opcao==1):
                resultado.append("Sim")
            elif(opcao==2):
                resultado.append("Não")
            elif(opcao==3):
                resultado.append("Poucas vezes")
            elif(opcao==4):
                break
            try:
                opcao = int(input("Você costuma ouvir gêneros musicais variádos: \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            except:
                print("Tente novamente")
                continue
            if (opcao==1):
                resultado.append("Sim")
            elif(opcao==2):
                resultado.append("Não")
            elif(opcao==3):
                resultado.append("Poucas vezes")
            elif(opcao==4):
                break
            try:
                opcao = int(input("Você usaria um app novo, no qual tocaria todas as suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            except:
                print("Tente novamente")
                continue
            if (opcao==1):
                resultado.append("Sim")
            elif(opcao==2):
                resultado.append("Não")
            elif(opcao==3):
                resultado.append("Poucas vezes")
            elif(opcao==4):
                break
            
            adicionar.writerow(resultado)
            arquivo = open("./Arquivo.csv", "a", newline="", encoding="utf-8")        
            arquivo.close()
            print("Arquivo criado!\n")
            break
def menu():
    import csv
    opcao=0
    while opcao !="00":
        print("\n     Dificulity Tecnologia e Informação ""\n""\n""1. Iniciar questionário \n2. Exibir resultado " "\n""00. Sair")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida! Tente novamente.")
            continue
        if  (opcao==1):
            entrevista() #Def para criar e editar o Arquivo CSV
        elif(opcao==2):
            with open("Módulo 2/Nova pasta/entrevista.csv", encoding="utf-8") as ler_arquivo:

            # 2. ler a tabela
                tabela = csv.reader(ler_arquivo, delimiter=",")

                # 3. navegar pela tabela
                for cont in tabela:        
                    print(" | ".join(cont))
                    break
                    #Aqui iremos ler o arquivo CSV com As respostas
        elif(opcao==00):
            print("\n""Aplicativo encerrado.\n")
            break
menu()
