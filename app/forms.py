from flask import request
from flask_wtf import FlaskForm
from werkzeug.datastructures import CombinedMultiDict, ImmutableMultiDict
from wtforms.fields.core import IntegerField, StringField
from wtforms.validators import DataRequired


class BaseForm(FlaskForm):
    method = 'POST'

    def __init__(self, *args, **kwargs):
        if not any([isinstance(arg, ImmutableMultiDict) for arg in args]):
            kwargs.setdefault('formdata', None)
        
        formdata = kwargs.get('formdata')
        if formdata and request.files:
            kwargs['formdata'] = CombinedMultiDict((formdata, request.files))
        
        self.css_class = None
        super().__init__(*args, **kwargs)


class SaveHighscoreForm(BaseForm):
    def __init__(self, *args, **kwargs):
        self.css_class = None
        super().__init__(*args, **kwargs)

    username = StringField(label='Username', validators=[DataRequired()])
    message = StringField(label='Message')

