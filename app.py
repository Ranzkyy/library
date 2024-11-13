import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template,request,redirect,jsonify,url_for
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://ranzkyy:ejaaja@cluster0.fbvbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.sertif

app = Flask(__name__)

@app.route('/')
def main():
    book_result = list(db.library.find({},{}))
    return render_template(
        'index.html',
        book=book_result
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/edit/<id>')
def edit_book(book_id):
    return render_template(
        'edit.html'
    )

@app.route('/add', methods=["POST"])
def add_book():
    title_book = request.form['title_book']
    author = request.form['author']
    year = request.form['year']
    doc = {
        'book' : title_book,
        'author' : author,
        'year' : year
    }
    db.library.insert_one(doc)
    return jsonify({'msg': 'Book saved'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)