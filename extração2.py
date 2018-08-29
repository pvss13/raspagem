import requests
from newspaper import Article

def cop():
    url = input('Cole a URL da notícia: ')
    a = Article(url, language='pt')
    a.download()
    a.parse()
    data = a.publish_date
    texto = a.text[:]
    autor = a.authors
    titulo = a.title
    resumo = a.summary
    
    return {
        'titulo': titulo,
        'resumo': resumo,
        'texto': texto,
        'autor': autor,
        'data': data
    }
        

def salvar(titulo, resumo, texto, autor, data):
    arquivo = open('pesquisa.csv', 'a')
    arquivo.write('%s,%s,%s,%s,%s\n' %(titulo,resumo,texto,autor,data)) 
    arquivo.flush()
    arquivo.close()
    
info = cop()
salvar(**info)
