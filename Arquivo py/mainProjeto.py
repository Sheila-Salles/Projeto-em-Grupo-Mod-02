from Projeto import Entrevista



perguntas = Entrevista()
perguntas.dados()
nome_do_arquivo = input("Digite o nome do arquivo .csv para guardar exemplo(""arquivo.csv""): ")
perguntas.salvar_arquivo_csv(nome_do_arquivo)