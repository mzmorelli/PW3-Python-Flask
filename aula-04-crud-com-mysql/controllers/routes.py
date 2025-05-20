from flask import render_template, request, redirect, url_for
from models.database import Game, db
from models.database import Console

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
                gamelist.append({'Título': request.form.get('titulo'), 'Ano': request.form.get(
                    'ano'), 'Categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    # rota de estoque (crud)
    @app.route('/estoquegames', methods=['GET', 'POST'])
    @app.route('/estoquegames/<int:id>')
    def estoquegames(id=None):
        # verificar se foi enviado alguma ID
        if id:
            # buscando jogo pela id e deletando
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoquegames'))
            
        # verificando se a requisição é POST
        # = -> atribuição
        # == -> comparação simples (valor)
        # === -> compara valor e tipo da variável
        if request.method == 'POST':
            # cadastra novo jogo
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'],
                           request.form['plataforma'], request.form['preco'], request.form['quantidade'])
            # enviando para o banco
            db.session.add(newgame)
            # confirmando as alterações
            db.session.commit()
            return redirect(url_for('estoquegames'))

        # fazendo um select no banco (pegando todos os jogos da tabela) / SELECT * from games
        gamesestoque = Game.query.all()
        return render_template('estoquegames.html',
                               gamesestoque=gamesestoque)
        
    @app.route('/estoqueconsoles', methods=['GET', 'POST'])
    @app.route('/estoqueconsoles/<int:id>')
    def estoqueconsoles(id=None):
        if id:
            console = Console.query.get(id)
            db.session.delete(console)
            db.session.commit()
            return redirect(url_for('estoqueconsoles'))
        
        if request.method == 'POST':
            newconsole = Console(request.form['nome'], request.form['fabricante'], request.form['preco'], request.form['quantidade'])
            db.session.add(newconsole)
            db.session.commit()
            return redirect(url_for('estoqueconsoles'))
        
        consoleestoque = Console.query.all()
        return render_template('estoqueconsoles.html',
                               consoleestoque=consoleestoque)

    # rota de edição de jogos
    @app.route('/editgame/<int:id>', methods=['GET', 'POST'])
    def editgame(id):
        game = Game.query.get(id)
        
        # editando o jogo com as informações vindas do formulário
        if request.method == 'POST':
            # coletando as informações do form
            game.titulo = request.form['titulo']
            game.ano = request.form['ano']
            game.categoria = request.form['categoria']
            game.plataforma = request.form['plataforma']
            game.preco = request.form['preco']
            game.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoquegames'))
                    
        return render_template('editgame.html', game=game)