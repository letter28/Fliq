from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('action', choices=['runserver', 'create_db'])
parser_args = parser.parse_args()

if __name__ == '__main__':
    if parser_args.action:
        if parser_args.action == 'runserver':
            from constants import HOST
            from app import app
            from utils import print_green
            print_green('Starting the app...')
            app.run(host=HOST)

        elif parser_args.action == 'create_db':
            from app import db
            from utils import print_green
            print_green('Creating the tables in the database...')
            db.create_all()
            print_green('Done!')
