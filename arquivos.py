#Função criada para carregar arquivos.
def carrega_arquivo(nome_arquivo, separador, tipos):
    f = open(nome_arquivo, 'r')
    linhas = f.readlines()
    cabecalho = linhas[0].replace('\n', '').split(separador)
    dados = linhas[1:]

    alunos = [] 

    for linha in dados:  
        dados_linha = linha.replace('\n', '').split(separador)
        aluno = {}  

        for index, tipo in enumerate(tipos):
            campo = cabecalho[index]

            if tipo == int:
                aluno[campo] = int(dados_linha[index])  
                aluno[campo] = float(dados_linha[index])  
            elif tipo == bool:
                if dados_linha[index] == 'True': 
                    aluno[campo] = True  
                else:
                    aluno[campo] = False  

        alunos.append(aluno)  

    f.close()  
    return alunos

#Função criada para Salvar o arquivo, caso façamos algum tipo de alteração.
def salvar_arquivo(nome_arquivo, separador, dados, cabecalho=None):
    f = open(nome_arquivo, 'w')

    if cabecalho is not None:
        cabecalho_str = separador.join(cabecalho) + '\n'  
        f.write(cabecalho_str)

    for linha in dados:
        linha_str = ''
        for coluna, valor in linha.items():
            linha_str += str(valor)
            if coluna != list(linha.keys())[-1]:  
                linha_str += separador
        linha_str += '\n'
        f.write(linha_str)

    f.close()  