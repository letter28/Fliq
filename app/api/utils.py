from flask import Response, json
from sqlalchemy.orm import class_mapper

from models import Users, UserHighscores, QuizQuestions


def json_response(data):
    if data:
        return Response(json.dumps(data, indent=2), mimetype='application/json')


def sql_model_to_json(model, hybrid_props=[]):
    columns = [c.key for c in class_mapper(model.__class__).columns] + [p for p in hybrid_props] if hybrid_props else []
    return dict((c, getattr(model, c)) for c in columns)


def get_all_users():
    users = Users.query.all()
    users = dict(users=[sql_model_to_json(user) for user in users])
    return json_response(users)


def get_all_highscores(limit=None):
    highscores = UserHighscores.query.order_by(
                    UserHighscores.score.desc(),
                    UserHighscores.date_of_score.asc()
                ).join(
                    Users,
                    Users.id == UserHighscores.user_id
                ).limit(limit).all()

    highscores = dict(highscores=[sql_model_to_json(score, hybrid_props=['username']) for score in highscores])
    return json_response(highscores)


def get_all_questions():
    questions = QuizQuestions.query.all()
    questions = dict(questions=[sql_model_to_json(question) for question in questions])
    return json_response(questions)
