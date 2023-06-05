from arquivos import carrega_arquivo
from processamento import filtro

separador = ','
tipos = [str , int , str , float , float , int , float , bool ]
nome_arquivo = r"/Users/jhenersonsilvadorosario/Documents/Workspace de Estudo VScode / Python - GrowDev/Processador_Dados/Dados/alunos.csv"

dados = carrega_arquivo(nome_arquivo, separador, tipos) # Exemplo de uso para carregar arquivos

dados_filtrados = filtro(dados, 'ano', 1, '>')
print(dados_filtrados) #Exemplo de uso para filtrar os dados.