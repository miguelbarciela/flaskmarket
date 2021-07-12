# EN TERMINAL:
# export FLASK_APP=market.py
# export FLASK_DEBUG=1 (solo en desarrollo, para que no haya que reiniciar servidor todo el rato)
# flask run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '6a0642d8cdb6390afcbd4bc9'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes