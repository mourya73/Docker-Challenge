from flask import Flask, jsonify

app = Flask(__name__)

# A list of books to be returned by the /api/books endpoint
books = [
    {'id': 1, 'title': 'Dune', 'author': 'Frank Herbert'},
    {'id': 2, 'title': 'Neuromancer', 'author': 'William Gibson'},
    {'id': 3, 'title': 'Ender\'s Game', 'author': 'Orson Scott Card'}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
