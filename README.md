Essa aplicação acessa uma pagina de pesquisa de um produto no Mercado Livre, é extrai o nome e valor de todos os produtos da pagina, e armazena em uma planilha em excel.

Esta sendo usando no exemplo uma pesquisa de 'Controle de Xbox Series' com o url da pesquisa: "https://lista.mercadolivre.com.br/controle-xbox-serie#D[A:controle%20xbox%20serie]"

A aplicação acessa a url com BeautifulSoup e faz as raspagem de dados de cada produto que aparece como resultado dessa pagina, e com Pandas armazena como dataframe e salva como uma planilha de excel.