TEMPLATE_FOLDER = '../templates/'
STATIC_URL_PATH = None

DATABASE = 'fliq'
PORT = 5432
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
SCHEMA = 'main_quiz'

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
