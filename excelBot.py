import pandas as pd

#1-CRIANDO ARQUIVO EXCEL

def criarExcel():
    #Criando dicionario para gerar tabela.
    pessoas = {'Nome':['Cida', 'Prado', 'LaraAL'],
     'ID':['100004079984833', '100041497221779', '100002862644818'],
      'Mensagem':['Oi tudo bem?', 'Oi Prado blza?', 'Tudo bem Lara?']
    }
    #Criando dados para armazenar no excel.
    dados = pd.DataFrame(data=pessoas)
    #Imprimindo na tela os dados da tabela. 
    #print(dados)
    #Gerando tabela excel.
    dados.to_excel('amigos.xls')

#2-PEGANDO DADOS DO ARQUIVO(TABELAS) EXCEL

def pegarTabela():
    #Passando o caminho do arquivo excel.
    arquivo = pd.read_excel('./amigos.xls')
    #Imprimindo o arquivo excel.
    #print(arquivo)
    #Imprimindo uma tabela especifica do arquivo.
    print(arquivo)
    #print(arquivo['Mensagem'])



#criarExcel()

#pegarTabela()

