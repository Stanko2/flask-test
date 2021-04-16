import os 

uri = os.environ.get('DATABASE_URL')


if 'sqlite' not in uri:
    # musime zmenit uri databazy, nakolko to defaultne nespolupracuje (v novej verzii sqlalchemy bolo zrusene)
    # a na heroku sa to zmenit neda
    uri.replace("://", "ql://", 1)

SQLALCHEMY_DATABASE_URI = uri
SQLALCHEMY_TRACK_MODIFICATIONS = False