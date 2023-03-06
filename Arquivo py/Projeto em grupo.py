import csv
import datetime

class Entrevista:
    def __init__(self):
        self.data = []
        self.cabecalho = ["Idade", "Gênero", "Pergunta_1", "Pergunta_2", "Pergunta_3", "Pergunta_4","Data e Hora"]

    def dados(self):
        print("\n     Empresa: Tecnologia e Dados   \n")
        idade = input("Digite a idade: ")
        while idade != "00":
            genero = input("Digite o gênero: ")
            pergunta_1 = input("Você costuma ouvir música por estações de rádio? \n1. Sim\n2. Não\n3. Poucas vezes\nDigite: ")                 
            pergunta_2 = (input("Você reserva um tempo do seu dia para ouvir suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes \nDigite: "))
            pergunta_3 = (input("Você costuma ouvir gêneros musicais variádos? \n1. Sim\n2. Não\n3. Poucas vezes\nDigite: "))
            pergunta_4 = (input("Você usaria um app novo, no qual tocaria suas músicas favoritas? \n1. Sim\n2. Não\n3. Poucas vezes\nDigite: "))
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
        print(f"{len(self.data)} dado(s) coletado(s) para pesquisa. O arquivo foi salvo como {nome}")
