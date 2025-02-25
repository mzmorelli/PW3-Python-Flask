from flask import render_template, request
# request serve para tratar as requisições do usuário

jogadores = ['Miguel José', 'Miguel Isack', 'Leaf', 'Quemario', 'Trop', 'Aspax', 'maxxdiego']

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = {
            'Título' : 'CS-GO',
            'Ano' : 2012,
            'Categoria' : 'FPS Online'
        }
        
        # tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # o append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
        
        jogos = ['Fortnite', 'Minecraft', 'Stray', 'The Legend of Zelda: Breath of The Wild', 'Baldurs Gate 3', 'Taiko no Tatsujin']
        return render_template('games.html',
                            game=game,
                            jogadores=jogadores,
                            jogos=jogos)