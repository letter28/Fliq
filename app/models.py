from sqlalchemy.util.langhelpers import hybridproperty

from app import db


class QuizQuestions(db.Model):
    __tablename__ = 'quiz_questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    choice_1 = db.Column(db.String)
    choice_2 = db.Column(db.String)
    choice_3 = db.Column(db.String)
    choice_4 = db.Column(db.String)
    answer = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id if self.id else '',
            'question': self.question if self.question else '',
            'choice_1': self.choice_1 if self.choice_1 else '',
            'choice_2': self.choice_2 if self.choice_2 else '',
            'choice_3': self.choice_3 if self.choice_3 else '',
            'choice_4': self.choice_4 if self.choice_4 else '',
            'answer': self.answer if self.answer else ''
            }


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)


class UserHighscores(db.Model):
    __tablename__ = 'quiz_highscores'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id))
    score = db.Column(db.Integer)
    category= db.Column(db.String)
    date_of_score = db.Column(db.DateTime)
    message = db.Column(db.String)

    @hybridproperty
    def username(self):
        if self.user_id:
            return Users.query.filter_by(id=self.user_id).first().username

    def to_dict(self):
        super().__init__(UserHighscores)

        yield('username', self.username if self.username else '')
