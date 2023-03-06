##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto em Grupo - Módulo 2 - – Quero os dados na minha mesa  #
#  Data de criação: 01/03/2023                                   #
#  Equipe: Diego, Erick, Robson, Sheila                          #
#  versão = '3.11'                                               #
##################################################################

########################################################################################################################
#                       Contexto                                                                                       #
#                                                                                                                      #
#   Nossa equipe recebeu uma nova solicitação de projeto!                                                              #
# Dessa vez para desenvolver uma pesquisa digital com a população de várias cidades do Brasil.                         #  
# Para isso, será necessário armazenar os dados dessa pesquisa em um arquivo .csv para utilização em análises futuras. #
# A pesquisa será feita a partir de um levantamento ativo,                                                             #
# realizado pelos funcionários da empresa que irão sair com o projeto nas ruas para coletar as respostas.              #
########################################################################################################################
#                                                                                                                      #
#                       Detalhes do projeto:                                                                           #             
#  A pesquisa que será realizada deve conter 4 perguntas (o grupo pode decidir o tema e formular as                    #
# questões) que podem ser respondidas com Sim (1), Não (2), Não sei responder (3).                                     #
#  Para iniciar o questionário será solicitado ao usuário que informe a sua idade e gênero. Cada                       #
# linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1, resposta_2, resposta_3,                          #
# resposta_4, data e hora da resposta                                                                                  #
#  O projeto deve ficar solicitando respostas em um laço de repetição que fica inserindo as                            #
# respostas informadas nas linhas do .csv até que a idade de 00 seja informada, então podemos                          #
# ficar inserindo novas respostas por quanto tempo for necessário (quando a idade 00 é informada                       #
# o projeto para de executar).                                                                                         #
########################################################################################################################

from Projeto import Entrevista

perguntas = Entrevista()
perguntas.dados()
nome_do_arquivo = input("Digite o nome do arquivo .csv para guardar exemplo(""arquivo.csv""): ")
perguntas.salvar_arquivo_csv(nome_do_arquivo)
