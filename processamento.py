#A função localizador retorna dados espeçificos de acordo com a linha que for adicionada nos parâmetros de uso da função.
def localizador (dados, linha):
    quantidade_registros = len(dados)
    if linha < quantidade_registros:
        return dados[linha]
    else:
        print("Indice superior a quantidade de registro no banco de dados!")
        return {}

#A função filtro permite filtrar os dados com base em uma coluna, um valor e uma operação. 
def filtro(dados, coluna, valor, operacao):
    dados_filtrados = []
    for linha in dados:
        if operacao == '==':
            if linha[coluna] == valor:
                dados_filtrados.append(linha)
        elif operacao == '!=':
            if linha[coluna] != valor:
                dados_filtrados.append(linha)
        elif operacao == '>':
            if linha[coluna] > valor:
                dados_filtrados.append(linha)
        elif operacao == '<':
            if linha[coluna] < valor:
                dados_filtrados.append(linha)
        elif operacao == '>=':
            if linha[coluna] >= valor:
                dados_filtrados.append(linha)
        elif operacao == '<=':
            if linha[coluna] <= valor:
                dados_filtrados.append(linha)
        else:
            raise ValueError("Operação não suportada: " + operacao)
    return dados_filtrados
#A função de projeção seleciona apenas as colunas desejadas dos dados e retorna uma nova lista de dicionários com essas colunas.
def projetar_dados(dados, colunas):
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for coluna in colunas:
            if coluna in linha:
                linha_projetada[coluna] = linha[coluna]
        dados_projetados.append(linha_projetada)
    return dados_projetados

#A função percorre cada registro na lista de dado e se o campo especificado estiver presente no registro, o valor desse campo é atualizado usando o parâmetro regra. 
def atualizar_registros(dados, campo, regra):
    for registro in dados:
        if campo in registro:
            registro[campo] = regra(registro[campo])
    
    return dados
#Essa função retorna um dicionário que irá conter os dados de um agrupamento específico definido pelo parâmetro chave.
def agrupamento(dados, chave):
    dados_agrupados = {}

    for linha in dados:
        valor_chave = linha[chave]
        
        if valor_chave in dados_agrupados:
            dados_agrupados[valor_chave].append(linha)
        else:
            dados_agrupados[valor_chave] = [linha]
    
    return [{chave: grupo} for chave, grupo in dados_agrupados.items()]