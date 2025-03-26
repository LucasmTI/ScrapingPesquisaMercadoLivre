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
df = pd.DataFrame()
produtos = soup.find_all('div', class_="poly-card__content")
for produto in produtos:
    nome = produto.find('h3', class_="poly-component__title-wrapper").get_text()
    valor = produto.find('span', class_="andes-money-amount__fraction").get_text()
    linha = pd.DataFrame([{'Nome' :nome, 'Valor' :valor}])
    df = pd.concat([df,linha], ignore_index=True)
df.to_excel("pesquisa.xlsx", index=False)
print(df)
