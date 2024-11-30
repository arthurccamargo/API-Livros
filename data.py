import requests
import pandas
import json

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

# Ler o arquivo CSV
df = pandas.read_csv("data_book.csv")

# Converter os dados para uma lista de dicionários
data = df.to_dict(orient="records")

# Estruturar os dados com a chave "books"
books_data = {"books": data}

# Salvar os dados em um arquivo JSON
with open("data_book.json", "w", encoding="utf-8") as json_file:
    json.dump(books_data, json_file, indent=4, ensure_ascii=False)

# Adicionar ID aos livros
for i, book in enumerate(books_data["books"], start=1):
    book["id"] = i

# Salvar IDs no arquivo JSON
with open("data_book.json", "w", encoding="utf-8") as json_file:
    json.dump(books_data, json_file, indent=4, ensure_ascii=False)
