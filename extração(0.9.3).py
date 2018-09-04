#----DEMOLIDOR DE CASTELOS----
#Banco de Dados de Notícias e Análise de Dados Coletados(ver:0.9.3)
#----Desenvolvedor: Paulo Vinicius Silva de Santana----
#E-mail: pvss13@gmail.com
#Program produced by a Portuguese speaker. If you need to contact us for any questions regarding the code. The function of the softwere is to capture the title and the text of news on the internet, joining with data such as author, website, session and time of the consultation (date and time) for later academic citation.

'''PRÓXIMOS PASSOS
criar e implantar função usando nltk
Steaming
Stopwords
Definir esquerda e direita
Definir precidenciáveis mencionados
Definir posicionamento com relação aos presidenciavies
Diferenciar texto jornalistico de Texto Opinativo
Diferenciar Liberal de Conservador
Diferenciar presença de incoerência no texto
Diferenciar texto embasado (com fontes) de texto sem fontes suficientes para sustentar os argumentos
Criar possibilidade de chamar a função para anlálise
Criar função busca (por data, por título, por data de raspagem, por hora de raspagem, por texto, por fonte, por autor(es)'''

#bibliotecas com necessidade de importação
from newspaper import Article
from datetime import datetime
        
#função de raspagem
def cop():
    url = input('Cole a URL da notícia:\n') #url a ser raspada
    now = datetime.now()
    dia = now.day #dia da consulta
    mes = now.month #Mẽs da consulta
    ano = now.year #Ano da Consulta
    horar = now.hour #Hora da consulta
    minuto = now.minute #minuto da consulta
    datac = ('%s/%s/%s' %(dia, mes, ano))
    horac = ('%s:%s' %(horar, minuto))

    site = input("Digite o nome do site:\n") #nome do portal
    editorial = input("Digite o nome do Editorial:\n") #editorial de origem da notícia
    autor = input("Digite o nome do autor(a) ou autores:\n") #autor da notícia
    a = Article(url, language='pt')
    a.download()
    a.parse()
    data = a.publish_date #data da publicação dentro do html no site
    texto = a.text[:] #texto presente no html do site
    texto = texto.replace('\n',' ') #tirando '\n' para não saltar linha no banco de dados em csv 
    titulo = a.title #título presente no html do site
    titulo = titulo.replace('\n',' ') #tirando '\n' do título para não saltar a linha no banco de dados em csv

    #retorno dos itens do banco de dados               
    return {
        'titulo': titulo,#título da reportage,(estou com problemas no csv pois a informação na fica na coluna correta)
        'texto': texto,#texto da reportagem (estou com problemas no csv que não fica numa única célula)
        'data': data,#data da publicação presente na reportagem
        'link': url,#a que foi fornecida anteriormente
        'datac': datac,#data da extração dos dados
        'horac': horac,#hora da extração dos dados
        'editorial': editorial,#coluna dentro do site
        'autor': autor,#autor do texto atribuido no site
        'site': site#local de extração dos dados
        
    }
        
'''def analise():'''
    

#função de salvamento
def salvar(autor, titulo, texto, data, link, datac, horac, site, editorial):
    arquivo = open('pesquisa.csv', 'a') #abrindo ou criando arquivo de banco de dados 'pesquisa.csv'
    arquivo.write('%s|%s|%s|%s|%s|%s|%s|%s|%s\n' %(autor, titulo,texto,data,link,datac,horac,site,editorial)) #separando item por '|' para não causar confusão na abertura do arquivo
    arquivo.flush()
    arquivo.close()

#função inicial
def ini():
    print("----DEMOLIDOR DE CASTELOS----\nBanco de Dados de Notícias (ver:0.9.3)") #cabeçalho do programa
    
    while True: #função de abertura do programa dando a opção de fechar o programa ou proceder na raspagem dos dados
        ini = input("\nDigite 1 (um) para raspar dados e digite 0 (zero) para sair:\nO que deseja fazer?\n")
        ini = int(ini)
        if ini==0:#o break é estabelecido pela saída do programa
            print("Saindo do programa.")
            exit()
            break
        if ini==1:
            print("\nRaspando dados\nDigite o link da notícia:")
            info = cop()
            salvar(**info)
        if ini!=1 and ini!=0:
            print("\nDigite uma opção válida! (0 ou 1)")

ini()
            
