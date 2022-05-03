import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import random

jsonData = json.load(open('questions.json', encoding="utf-8"))

app = Flask(__name__)
app.secret_key = "don't tell anyone"
api = Api(app)
ENV = 'dev'

if ENV == 'dev':
    config = str(open('configlocal.txt', 'r').read())
    app.debug = True
else:
    config = open('configheroku.txt', 'r').read()
    app.debug = False

app.config['SQLALCHEMY_DATABASE_URI'] = config
bylo = []

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    nsfw = db.Column(db.String)
    questions = db.Column(db.String)

    def __init__(
        self, id, name,
        nsfw, questions
    ):
        self.id = id
        self.name = name
        self.nsfw = nsfw
        self.questions = questions


class Categories_api(Resource):
    def get(self):
        data = []
        for category in Category.query.all():
            data.append({
                "id": category.id,
                "name": category.name,
                "nsfw": category.nsfw,
                "questions": list(category.questions.split('nextquestion'))}
            )
        return data


class Question_api(Resource):
    def get(self):
        args = request.args
        for arg in args:
            if arg == "category":
                data = Category.query.filter_by(
                    name=args.get(arg)).first().questions
                data = list(data.split('nextquestion'))
                rand = random.randint(0, len(data))
                return data[rand]


api.add_resource(Categories_api, "/api/categories")
api.add_resource(Question_api, "/api/question")


def addToDataBaseFromJSON(jsonData):
    for x in jsonData:
        data = Category(
            x["id"],
            x["category"],
            x["nsfw"],
            'nextquestion'.join([str(item).replace('"', '').replace(
                "'", "") for item in x["questions"]])
        )
        db.session.add(data)
        db.session.commit()

# addToDataBaseFromJSON(jsonData)


if __name__ == '__main__':
    app.run()
