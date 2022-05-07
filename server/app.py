import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import random

json_data = json.load(open('questions.json', encoding="utf-8"))

# NEEDS TO BE CHANGED AFTER ADDING/DELETNING A CATEGORY
categories_count = 8


app = Flask(__name__)
app.secret_key = "don't tell anyone"
api = Api(app)
ENV = 'prod'

if ENV == 'dev':
    config = str(open('configlocal.txt', 'r').read())
    app.debug = True
else:
    config = open('configheroku.txt', 'r').read()
    app.debug = False

app.config['SQLALCHEMY_DATABASE_URI'] = config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db = SQLAlchemy(app)


def random_questions(par, value, count):
    print(value)
    if par == "category":
        data = Card.query.filter_by(
                            category=value).first()
    elif par == "id":
        data = Card.query.filter_by(
                            id=value).first()
    category = data.category
    data = data.questions
    data = list(data.split(';'))
    return_data = []
    if count > len(data):
        count = len(data)
    for i in range(0, count):
        question = data[random.randint(0, len(data)-1)]
        while question in return_data:
            question = data[random.randint(0, len(data)-1)]
        return_data.append(({
                    "category": category,
                    "question": question
                    }))
    return return_data


class Card(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.String, primary_key=True)
    category = db.Column(db.String)
    nsfw = db.Column(db.Boolean)
    questions = db.Column(db.String)

    def __init__(
        self, id, category,
        nsfw, questions
    ):
        self.id = id
        self.category = category
        self.nsfw = nsfw
        self.questions = questions


class All_cards_api(Resource):
    def get(self):
        data = []
        for card in Card.query.all():
            data.append({
                "category": card.category,
                "nsfw": card.nsfw,
                "number_of_questions": len(list(
                    card.questions.split(';'))
                    )}
            )
        return {"items": data}


class Select_cards_api(Resource):
    def get(self):
        args = request.args
        count = 1
        ret_data = []
        if "count" in args:
            count = int(args.get("count"))
        if "category" in args:
            categories = (args.get("category").split(','))
            for category in categories:
                if category != "random":
                    for question in random_questions("category", category, count):
                        ret_data.append(question)
        if "category" not in args or "random" in categories:
            for question in random_questions("id", str(random.randint(1, categories_count)), count):
                ret_data.append(question)
        random.shuffle(ret_data)
        return {
            "totalItems": len(ret_data[0:count]),
            "items": ret_data[0:count]
            }


api.add_resource(All_cards_api, "/api/categories")
api.add_resource(Select_cards_api, "/api/question")


def add_to_database_from_json(json_data):
    for x in json_data:
        data = Card(
            x["id"],
            x["category"],
            x["nsfw"],
            ';'.join([item for item in x["questions"]])
        )
        db.session.add(data)
        db.session.commit()

#add_to_database_from_json(json_data)


if __name__ == '__main__':
    app.run()
