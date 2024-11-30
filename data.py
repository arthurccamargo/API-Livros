import requests
import pandas

# Capturando os livros da API Google Books que possuem no titulo a palavra "data science"
response = requests.get(url="https://www.googleapis.com/books/v1/volumes?q=data%20science")
response.raise_for_status()
books = response.json()

title_list = []
authors_list = []
description_list = []
selfLink_list = []
pageCount_list = []

for book in books["items"]:
    title_list.append(book["volumeInfo"]["title"])
    authors_list.append(book["volumeInfo"]["authors"])
    description_list.append(book["volumeInfo"]["description"])
    selfLink_list.append(book["selfLink"])

# Estruturar os dados dos livros no dict 
data_dict = {
    "title":title_list,
    "authors": authors_list,
    "description":description_list,
    "selfLink":selfLink_list,
}

# Criacao do DataFrame
data = pandas.DataFrame(data_dict)

# Salvar no arquivo .csv sem a coluna Unnamed
data.to_csv("data_book.csv", index=False)