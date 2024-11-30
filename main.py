import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
requisicao = requests.get(link)
print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")  # Organiza o código
print(site.prettify())

# Link do projeto https://www.youtube.com/watch?v=WzUPnQwSQyk
# Pausado em 16:43
