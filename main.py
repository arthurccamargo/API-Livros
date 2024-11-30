from flask import Flask, make_response, jsonify
import json

# Ler o arquivo JSON
with open("data_book.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Extrai o conteudo dentro de "books"
books = data["books"]

# Instacia de Flask em app  
app = Flask(__name__)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_books(book_id): # Parametro do caminho
    # Buscar o livro pelo ID, devolve None se nao encontrar
    book = next((book for book in books if book["id"] == book_id), None)

    if book:
        return make_response(jsonify(book), 200)
    else:
        return make_response(
            jsonify({'error':f'Book with id {book_id} not found'}), 404
        )


# Executa servidor flask
if __name__ == '__main__':
    app.run(debug=True) 
