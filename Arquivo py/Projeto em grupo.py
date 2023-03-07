import csv
import datetime

class Entrevista:
    def __init__(self):
        self.data = []
        self.cabecalho = ["Idade", "Gênero", "Pergunta_1", "Pergunta_2", "Pergunta_3", "Pergunta_4","Data e Hora"]

    def dados(self):
        print("\n     Empresa: Tecnologia e Dados   \n")
        idade = (input("Digite a idade: "))  
        while idade != "00":
            try:
                genero = int(input("Selecione o gênero: \n1. Feminino \n2. Masculino \n3. Outros \nOpção: "))
                if (genero == 1):
                    genero = ("Feminino")
                elif (genero == 2):
                    genero = ("Masculino")
                elif (genero == 3):
                    genero=("Outros")                  
            except:
                print("Opção inválida. Tente novamente.")
                continue                                
            try:
                pergunta_1 = int(input("Você costuma ouvir música por estações de rádio? \n1. Sim\n2. Não\n3. Poucas vezes\nOpção: "))                 
                if (pergunta_1 == 1):
                    pergunta_1 = ("Sim")
                elif (pergunta_1 == 2):
                    pergunta_1 = ("Não")
                elif (pergunta_1 == 3):
                    pergunta_1=("Poucas vezes")
            except:
                print("Opção inválida. Tente novamente.")
                continue    
            try:
                pergunta_2 = int(input("Você reserva um tempo do seu dia para ouvir suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes \nOpção: "))
                if (pergunta_2 == 1):
                    pergunta_2 = ("Sim")
                elif (pergunta_2 == 2):
                    pergunta_2 = ("Não")
                elif (pergunta_2 == 3):
                    pergunta_2=("Poucas vezes")
            except:
                print("Opção inválida. Tente novamente.")
                continue  
            try:    
                pergunta_3 = int(input("Você costuma ouvir gêneros musicais variádos? \n1. Sim\n2. Não\n3. Poucas vezes\nOpção: "))
                if (pergunta_3 == 1):
                    pergunta_3 = ("Sim")
                elif (pergunta_3 == 2):
                    pergunta_3 = ("Não")
                elif (pergunta_3 == 3):
                    pergunta_3=("Poucas vezes")
            except:
                print("Opção inválida. Tente novamente.")
                continue  
            try:
                pergunta_4 = int(input("Você usaria um app novo, no qual tocaria suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes\nOpção: "))
                if (pergunta_4 == 1):
                    pergunta_4 = ("Sim")
                elif (pergunta_4 == 2):
                    pergunta_4 = ("Não")
                elif (pergunta_4 == 3):
                    pergunta_4=("Poucas vezes")
            except:
                print("Opção inválida. Tente novamente.")
                continue
                            
            now = datetime.datetime.now()
            data_hora = now.strftime("%d/%m/%Y %H:%M:%S")
            lista = [idade, genero, pergunta_1, pergunta_2, pergunta_3, pergunta_4, data_hora]
            self.data.append(lista)
            idade = input("Digite a idade ou '00' para encerrar: ")
            
            
    def salvar_arquivo_csv(self, nome):
        with open(nome, "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(self.cabecalho)
            writer.writerows(self.data)
        print(f"{len(self.data)} dado(s) coletado(s) para a pesquisa. O arquivo foi salvo como {nome}")
