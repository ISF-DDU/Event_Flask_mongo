from flask import Flask, render_template, request, redirect
from datetime import datetime
import pymongo
import uuid


app = Flask(__name__)


def get_database():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['my_diary']
    collection = db['diaries']
    return collection


@app.route('/')
def hello_world():
    collection = get_database()
    posts = collection.find()

    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        time = datetime.now()
        collection = get_database()
        
        data = {
            "_id": uuid.uuid4().hex,
            "title" : title,
            "description": description,
            "time": time
        }

        collection.insert_one(data)

        return redirect('/')
    return render_template('create_post.html')


@app.route('/update/<id>', methods=('GET', 'POST'))
def update_post(id):
    collection = get_database()
    post = collection.find_one({"_id": id})
    
    if request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")
        time = datetime.now()

        data = {
            "$set": {
                "title": title,
                "description": description,
                "time": time
            }
        }

        collection.update_one(post, data)

        return redirect('/')
    return render_template('update_post.html', post=post)


@app.route('/delete/<id>')
def delete_post(id):
    collection = get_database()

    collection.delete_one({"_id": id})

    return redirect('/')

app.run(debug=True)