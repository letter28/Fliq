
from database.db_session import db_session
from database.models import QuizQuestions, UserHighscores

from os import getcwd, path
import random
import math
import requests
import json
from html import unescape


def get_user_highscores(limit=10):
    try:
        scores = UserHighscores.query.order_by(
            UserHighscores.score.desc(),
            UserHighscores.category.asc(),
            UserHighscores.date_of_score.asc()).limit(limit).all()
        return scores
    except Exception as e:
        print(str(e))


def get_n_random_questions(n):
    if n:
        num_questions = db_session.query(QuizQuestions.id).count()
        if num_questions:
            questions = []
            random_ids = [math.floor(random.random() * num_questions) for i in range(n)]

            random_questions = db_session.query(QuizQuestions).filter(QuizQuestions.id.in_([1])).all()
            for q in random_questions:
                questions.append(q.to_dict())
            return questions
    return None


def fetch_api_data(url):
    response = requests.get(url=url)
    if response:
        return response.text
    return None


def parse_and_save_questions(response_text):
    if response_text:
        new_questions = []
        questions_json = json.loads(response_text)
        results = questions_json['results']
        for result in results:
            question = dict(question=unescape(result.get('question')))
            new_question = make_a_question(
                                    question=question,
                                    answers=result.get('incorrect_answers'),
                                    correct_answer=result.get('correct_answer')
                                    )
            new_questions.append(new_question)

        with open('static/resources/questions.json', 'w', encoding='ascii') as fout:
            json.dump(new_questions, fout)


def make_a_question(question: dict, answers: list, correct_answer: str):
    random_index = random.randint(0, 3)
    answers.insert(random_index, correct_answer)
    question.update(
        answer=random_index + 1,
        choice1=unescape(answers[0]),
        choice2=unescape(answers[1]),
        choice3=unescape(answers[2]),
        choice4=unescape(answers[3]),
    )
    return question