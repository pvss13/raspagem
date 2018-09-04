#----DEMOLIDOR DE CASTELOS----
#Banco de Dados de Notícias e Análise de Dados Coletados(ver:0.9.2)
#----Desenvolvedor: Paulo Vinicius Silva de Santana----
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


from newspaper import Article
from datetime import datetime
        
#função de raspagem
def cop():
    url = input('Cole a URL da notícia:\n')
    now = datetime.now()
    dia = now.day
    mes = now.month
    ano = now.year
    horar = now.hour
    minuto = now.minute
    datac = ('%s/%s/%s' %(dia, mes, ano))
    horac = ('%s:%s' %(horar, minuto))

    site = input("Digite o nome do site:\n")
    editorial = input("Digite o nome do Editorial:\n")
    autor = input("Digite o nome do autor(a) ou autores:\n")
    a = Article(url, language='pt')
    a.download()
    a.parse()
    data = a.publish_date
    texto = a.text[:]
    texto = texto.replace('\n',' ')
    titulo = a.title
    titulo = titulo.replace('\n',' ')
                   
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
    arquivo = open('pesquisa.csv', 'a')
    arquivo.write('%s|%s|%s|%s|%s|%s|%s|%s|%s\n' %(autor, titulo,texto,data,link,datac,horac,site,editorial)) 
    arquivo.flush()
    arquivo.close()

#função inicial
def ini():
    print("----DEMOLIDOR DE CASTELOS----\nBanco de Dados de Notícias (ver:0.9)")
    
    while True:
        ini = input("\nDigite 1 (um) para raspar dados e digite 0 (zero) para sair:\nO que deseja fazer?\n")
        ini = int(ini)
        if ini==0:
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
            
