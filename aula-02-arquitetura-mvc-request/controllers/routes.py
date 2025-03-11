from flask import render_template, request, redirect, url_for
# request serve para tratar as requisições do usuário

jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# array de objetos - lista de games
gamelist = [{
            'Título': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'
            }]

consolelist = [{
    'Nome' : 'Playstation',
    'Fabricante' : 'Sony',
    'Ano' : 1994,
    'Preço' : 500
}]


def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # o append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
                return redirect(url_for('games'))

        jogos = ['Fortnite', 'Minecraft', 'Stray',
                 'The Legend of Zelda: Breath of The Wild', 'Baldurs Gate 3', 'Taiko no Tatsujin']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)

    # rota de cadastro de jogos (em dicionario)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título': request.form.get('titulo'),
                                 'Ano': request.form.get('ano'),
                                 'Categoria': request.form.get('categoria')})
                return redirect(url_for('games'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('fabricante') and request.form.get('ano') and request.form.get('preco'):
                consolelist.append({'Nome': request.form.get('nome'),
                                 'Fabricante': request.form.get('fabricante'),
                                 'Ano': request.form.get('ano'),
                                 'Preço': request.form.get('preco')})
                return redirect(url_for('consoles'))
        return render_template('consoles.html',
                               consolelist=consolelist)
