from flask import render_template, request, redirect, url_for
from models.database import Game, Console
# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5', 'Jogo 6']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
    
    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    #Rota de Estoque (CRUD)
    @app.route('/estoque')
    def estoque():
        
        #criando um select no banco, todos os jogos da tabela: Game.delete, Game.add, Game.querry.all. GRAVADO NA VARIAVEL GAMESESTOQUE
        gamesestoque = Game.query.all()
        consoleestoque = Console.query.all()
        return render_template('estoque.html',
                               gamesestoque=gamesestoque,
                               consoleestoque=consoleestoque)
        