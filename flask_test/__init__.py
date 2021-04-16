from flask import Flask
from .extensions import db;
from .commands import create_tables;

def create_app(cfg='Settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile('Settings.py')
    db.init_app(app)

    app.cli.add_command(create_tables)


    @app.route('/')
    def hello():
        return 'hello'

    # @app.route('/<name>/<pass>')
    # def add_user(name, pass):

    return app
