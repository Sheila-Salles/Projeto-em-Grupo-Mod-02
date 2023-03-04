import csv
import datetime

class Entrevista:
    def __init__(self):
        self.data = []
        self.cabecalho = ["Idade", "Gênero", "Pergunta_1", "Pergunta_2", "Pergunta_3", "Pergunta_4","Data e Hora"]

    def dados(self):
        sim = ("Sim")
        nao = ("Não")
        pouco = ("Poucas vezes")
        idade = input("Digite a idade: ")
        genero = input("Digite o gênero: ")
        idade = 0
        while idade != "00":
            
            try:
                pergunta_1 = input("Você costuma ouvir música por estações de rádio? \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: ")
            except:
                print("Tente novamente")
                continue
            if (idade=="1"):
                pergunta_1 = ("Sim")
            elif(idade==2):
                pergunta_1 = nao
            elif(idade==3):
                pergunta_1 = pouco
                             
            pergunta_2 = int(input("Você reserva um tempo do seu dia para ouvir suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            pergunta_3 = int(input("Você costuma ouvir gêneros musicais variádos? \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            pergunta_4 = int(input("Você usaria um app novo, no qual tocaria suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes \n4. Voltar\nOpção: "))
            now = datetime.datetime.now()
            data_hora = now.strftime("%d/%m/%Y %H:%M:%S")
            lista = [idade, genero, pergunta_1, pergunta_2, pergunta_3, pergunta_4, data_hora]
            self.data.append(lista)
            idade = input("Digite sua idade ou '00' para encerrar: ")
            break

    def salvar_arquivo_csv(self, nome):
        with open(nome, "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(self.cabecalho)
            writer.writerows(self.data)
        print(f"{len(self.data)} dado(s) coletado(s) para pesquisa. O arquivo foi salvo como {nome}")
    

