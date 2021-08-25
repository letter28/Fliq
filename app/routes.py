from flask import render_template, redirect, request, Blueprint, url_for, flash
from datetime import datetime

from constants import OPEN_TRIVIA_URL, categories
from forms import SaveHighscoreForm
from app import db
from models import UserHighscores, Users
from utils import fetch_api_data, parse_and_save_questions, get_user_highscores


app_blueprint = Blueprint('index', __name__)


@app_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app_blueprint.route('/play-quiz/<cat_num>', methods=['GET'])
def play_quiz(cat_num):
    if cat_num:
        category = categories[cat_num]
        resp = fetch_api_data(OPEN_TRIVIA_URL % cat_num)
        if resp:
            parse_and_save_questions(resp)

            return render_template('quiz.html', question={}, category=category)
    return redirect('/')


@app_blueprint.route('/highscores', methods=['GET', 'POST'])
def highscores():
    scores = get_user_highscores()
    if scores:
        return render_template('highscores.html', scores=scores)
    return redirect('/')


@app_blueprint.route('/save-score', methods=['POST', 'GET'])
def save_score():
    if request.method == 'GET':
        return redirect(url_for('index.highscores'))

    if request.method == "POST":
        score_data = request.get_json()

        username = score_data['username']
        if username:
            user = Users.query.filter_by(username=username).first()

            if not user:
                user = Users(username=username)
                db.session.add(user)
                db.session.commit()

            user_id = user.id

            new_score = UserHighscores(
                user_id=user_id,
                message=score_data['message'],
                score=score_data['score'],
                category=score_data['category'],
                date_of_score=datetime.now()
            )

            db.session.add(new_score)
            db.session.commit()

            return redirect(url_for('index.highscores'))


@app_blueprint.route('/quiz-results', methods=['GET', 'POST'])
def quiz_results():
    if request.method == 'GET':
        return render_template('results.html', scores=get_user_highscores(), form=SaveHighscoreForm())

    if request.method == 'POST':
        score_form = SaveHighscoreForm(formdata=request.form)

        if score_form.validate():
            flash('Score saved successfully!', 'success')
            return redirect(url_for('index.save_score'))
        else:
            flash(score_form.errors, 'danger')

    return redirect(request.referrer)

