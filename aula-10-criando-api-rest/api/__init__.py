from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# adicionando os recursos da api
from .resources import game_resources