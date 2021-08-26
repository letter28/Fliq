import os

TEMPLATE_FOLDER = '../templates/'
STATIC_URL_PATH = '/static'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_PSWRD = os.environ.get('DB_PSWRD')
DB_SCHEMA = os.environ.get('DB_SCHEMA')

OPEN_TRIVIA_URL = 'https://opentdb.com/api.php?amount=10&category=%s&type=multiple'

categories = {
    '9': 'General knowledge',
    '17': 'Science and nature',
    '20': 'Mythology',
    '21': 'Sports',
    '22': 'Geography',
    '23': 'History',
    '25': 'Art',
    '27': 'Animals'
}

class BCOLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
