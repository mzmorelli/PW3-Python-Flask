# importando a classe resource do flask_restful
from flask_restful import Resource
# importando a api
from api import api

# logo abaixo irá as respostas da API
class GameList(Resource):
    def get(self):
        return {
            "games": [
                {"name": "The Legend of Zelda: Breath of the Wild", "platform": "Nintendo Switch"},
                {"name": "God of War", "platform": "PlayStation 4"},
                {"name": "Red Dead Redemption 2", "platform": "PlayStation 4, Xbox One, PC"},
            ]
        }

# criando o endpoint (rota) principal da api
api.add_resource(GameList, "/games")