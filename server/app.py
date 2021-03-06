import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import random

ENV = 'prod'
app = Flask(__name__)
app.secret_key = "don't tell anyone"
api = Api(app)


if ENV == 'dev':
    config = open('configlocal.txt', 'r').read()
    app.debug = True
elif ENV == 'prod':
    config = open('configheroku.txt', 'r').read()
    app.debug = False

app.config['SQLALCHEMY_DATABASE_URI'] = config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db = SQLAlchemy(app)


def random_questions(value, count):
    print(value)
    card = Card.query.filter_by(
        category=value).first()
    category = card.category
    name = card.name
    card = list(card.questions.split(';'))
    return_data = []
    if count > len(card):
        count = len(card)
    for i in range(0, count):
        question = card[random.randint(0, len(card)-1)]
        while {
            "category": category,
            "name": name,
            "question": question
                } in return_data:
            question = card[random.randint(0, len(card)-1)]
        return_data.append(({
                    "category": category,
                    "name": name,
                    "question": question
                    }))
    return return_data


def random_questions_random_category(count, nsfw):
    return_data = []
    data = Card.query.all()
    for i in range(count):
        card = data[
            random.randint(0, len(data)-1)
            ]
        while card.nsfw != nsfw:
            card = data[
                random.randint(0, len(data)-1)          
            ]
        category = card.category
        name = card.name
        questions = list(card.questions.split(';'))
        question = questions[random.randint(0, len(questions)-1)]
        while {
            "category": category,
            "name": name,
            "question": question
                } in return_data:
            question = questions[random.randint(0, len(questions)-1)]
        return_data.append(({
                        "category": category,
                        "name": name,
                        "question": question
                        }))
    return return_data


class Card(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.String, primary_key=True)
    category = db.Column(db.String)
    name = db.Column(db.String)
    nsfw = db.Column(db.Boolean)
    questions = db.Column(db.String)

    def __init__(
        self, id, category, name,
        nsfw, questions
    ):
        self.id = id
        self.category = category
        self.name = name
        self.nsfw = nsfw
        self.questions = questions


class All_cards_api(Resource):
    def get(self):
        return_data = []
        for card in Card.query.all():
            return_data.append({
                "category": card.category,
                "name": card.name,
                "nsfw": card.nsfw,
                "number_of_questions": len(list(
                    card.questions.split(';'))
                    )}
            )
        return {"items": return_data}


class Select_cards_api(Resource):
    def get(self):
        args = request.args
        count = 1
        return_data = []
        nsfw = bool(random.getrandbits(1))
        if "nsfw" in args:
            nsfw = args.get("nfw")
        if "count" in args:
            count = int(args.get("count"))
        if "category" in args:
            categories = (args.get("category").split(','))
            for category in categories:
                if category != "random":
                    for question in random_questions(category, count):
                        return_data.append(question)
        if "category" not in args or "random" in categories:
            for question in random_questions_random_category(count, bool(nsfw)):
                return_data.append(question)
        random.shuffle(return_data)
        return {
            "totalItems": len(return_data[0:count]),
            "items": return_data[0:count]
            }


api.add_resource(All_cards_api, "/api/categories")
api.add_resource(Select_cards_api, "/api/question")


def add_to_database_from_json(json_data):
    for cards in json_data:
        data = Card(
            cards["id"],
            cards["category"],
            cards["name"],
            cards["nsfw"],
            ';'.join([item for item in cards["questions"]])
        )
        db.session.add(data)
        db.session.commit()


def create_table():
    with open('questions.json', encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    db.create_all()
    add_to_database_from_json(json_data)


if __name__ == '__main__':
    app.run()
