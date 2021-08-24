from flask import Blueprint, request

from api.utils import get_all_highscores


api_blueprint = Blueprint('api', __name__, url_prefix='/api')


@api_blueprint.route('/highscores/<limit>', methods=['GET'])
def highscores(limit):
    if request.method == 'GET':
        return get_all_highscores(limit)
