import requests
from bs4 import BeautifulSoup
import pandas as pd

# função para transformar o request em dados em html
def trazer_html(url):
    resposta = requests.get(url).text
    return resposta


url = r"https://lista.mercadolivre.com.br/controle-xbox-serie#D[A:controle%20xbox%20serie]"

pagina = trazer_html(url) # chamando a função para transformar em html
soup = BeautifulSoup(pagina,'html.parser')
df = pd.DataFrame() # criando um dataframe vazio
produtos = soup.find_all('div', class_="poly-card__content") # separando os produtos em uma lista
for produto in produtos: # pegando o nome, preço e link de cada produto.
    nome = produto.find('h3', class_="poly-component__title-wrapper").get_text()
    valor = produto.find('span', class_="andes-money-amount__fraction").get_text()
    link = produto.find('a').get('href')
    linha = pd.DataFrame([{'Nome' :nome, 'Valor' :valor, 'Link' : link}]) # transformadno o resultado em uma linha em dataframe
    df = pd.concat([df,linha], ignore_index=True) # adicionando a linha no dataframe de cada produto encontrado.
df.to_excel("pesquisa.xlsx", index=False) # Salvando a em planilha em excel com o resultado.
print(df)
