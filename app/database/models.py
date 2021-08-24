from sqlalchemy import String, Integer, Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.util.langhelpers import hybridproperty

from database.db_session import Base


class QuizQuestions(Base):
    __tablename__ = 'quiz_questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    choice_1 = Column(String)
    choice_2 = Column(String)
    choice_3 = Column(String)
    choice_4 = Column(String)
    answer = Column(Integer)

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


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)


class UserHighscores(Base):
    __tablename__ = 'quiz_highscores'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Users.id))
    score = Column(Integer)
    category= Column(String)
    date_of_score = Column(DateTime)
    message = Column(String)

    @hybridproperty
    def username(self):
        if self.user_id:
            return Users.query.filter_by(id=self.user_id).first().username
    
    def to_dict(self):
        super().__init__(UserHighscores)

        yield('username', self.username if self.username else '')
