from flask import Flask
from flask_test.extensions import db;
from flask_test.commands import create_tables;
from flask_test.models import User

def create_app(cfg='Settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile('Settings.py')
    db.init_app(app)

    app.cli.add_command(create_tables)


    @app.route('/')
    def hello():
        return 'hello'

    @app.route('/<name>/<passw>')
    def add_user(name, passw):
        user = User(name = name, password = passw)
        db.session.add(user)
        db.session.commit()
        return 'success'
    
    @app.route('/users')
    def list_users():
        users = User.query.filter().all()
        return '\n'.join(map(lambda x: f'name: {x.name}', users))

    return app
