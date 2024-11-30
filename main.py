import pandas
import json

# Ler o arquivo CSV
df = pandas.read_csv("data_book.csv")

# Converter os dados para uma lista de dicionários
data = df.to_dict(orient="records")

# Estruturar os dados com a chave "books"
books_data = {"books": data}

# Salvar os dados em um arquivo JSON
with open("data_book.json", "w", encoding="utf-8") as json_file:
    json.dump(books_data, json_file, indent=4, ensure_ascii=False)