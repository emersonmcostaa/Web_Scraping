import json

import requests
from bs4 import BeautifulSoup


url = 'https://www.bibliaonline.com.br/nvi'
response = requests.get(url)
site = BeautifulSoup(response.content, 'html.parser')

# Tag dos livros da biblia:
livros_geral = site.find('div', attrs={'class': 'jss50'})
# Pegar todos os livros:
list_livros_tags = livros_geral.findAll('a', attrs={'class': 'jss29 jss53'})
# Criar dicionario:
dic_livros = {}

for tag in list_livros_tags:
    livro = tag.text
    link_livro = tag['href']
    # Colocar livro e link dentro do dicionario
    dic_livros[livro] = link_livro

# Gerar arquivo json:
with open('livros_bilia_link.json', 'w', encoding='utf_8') as fp:
    json.dump(dic_livros, fp, indent=4, ensure_ascii=False)
