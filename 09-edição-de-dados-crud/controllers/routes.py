from flask import render_template, request, redirect, url_for
from models.database import Game, Console, db


# lista de jogadores 
jogadores = ['miguel josé', 'miguel isack', 'leaf',
             'aspax', 'quemario', 'trop', 'maxxdiego']
# array de objetos -> lista de games
gameList = [{
            'titulo': 'CS-GO',
            'ano': 2012,
            'categoria': 'FPS Online',
            }]

consoleList = [{
    'nome' : 'Xbox One Fat',
    'fabricante' : 'Microsoft',
    'ano' : 2013,
    'preco' : 'caro'
}]


def init_app(app):
    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gameList[0]
        # tratando se a request for post
        if request.method == 'POST':
            # verificar se o campo de jogador existe
            if request.form.get('jogador'):
                # adicionando um novo jogador com append
                jogadores.append(request.form.get('jogador'))
                return redirect(url_for('games'))

        jogosFriv = ['Fireboy & Watergirl', "Papa's pizzaria",
                    'Motox3m', 'Bob the Robber', 'Temple Run 2', 'Dynamon']

        return render_template('games.html',
                            game=game,
                            jogadores=jogadores,
                            jogosFriv=jogosFriv)

    # rota de cadastro de games em dicionário
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                # adicionando um novo game com append
                gameList.append({
                    'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria')
                })
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html', 
                            gameList=gameList,
                            )

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        if request.method == 'POST':
            if request.form.get("nome") and request.form.get("fabricante") and request.form.get("ano") and request.form.get("preco"):
                consoleList.append({
                    'nome' : request.form.get('nome'),
                    'fabricante' : request.form.get('fabricante'),
                    'ano' : request.form.get('ano'),
                    'preco' : request.form.get('preco')
                })
            return redirect(url_for('consoles'))
        
        return render_template("consoles.html", 
                            consoleList = consoleList
                            )

    # rota de estoque (CRUD)
    @app.route('/estoqueGames', methods=['GET', 'POST'])
    @app.route('/estoqueGames/<int:id>')
    def estoqueGames(id=None, type=""):
        if id:
            # buscando o jogo pela id
            game=Game.query.get(id)
            # deletando o jogo
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoqueGames'))
        

        # = atribuição
        # == comparação de valor
        # === comparação de tipo e valor
        # Verificandose a requisição é POST:
        if request.method == 'POST' and request.form.get("CadastrarJogo") == "true":
            # cadastrando o novo jogo
            newGame = Game(request.form['title'],
                           request.form['year'], 
                           request.form['category'], 
                           request.form['platform'], 
                           request.form['price'], 
                           request.form['quantity'], 
                           )
            # Enviando para o banco
            db.session.add(newGame)
            # Confirmando as alterações
            db.session.commit()
            return redirect(url_for('estoqueGames'))
        
        
        
            
        
        # fazendo um SELECT no banco (pegando todos os jogos da tabela)
        gamesestoque = Game.query.all()
        return render_template('estoqueGames.html', gamesestoque=gamesestoque)
    
    # rota de estoque (CRUD)
    @app.route('/estoqueConsoles', methods=['GET', 'POST'])
    @app.route('/estoqueConsoles/<int:id>')
    def estoqueConsoles(id=None, type=""):
        if id:
            # buscando o jogo pela id
            console=Console.query.get(id)
            # deletando o jogo
            db.session.delete(console)
            db.session.commit()
            return redirect(url_for('estoqueConsoles'))
        

        # = atribuição
        # == comparação de valor
        # === comparação de tipo e valor
        # Verificandose a requisição é POST:
        if request.method == 'POST' and request.form.get("CadastrarConsole") == "true":
            # cadastrando o novo console
            newConsole = Console(request.form['name'],
                           request.form['producer'], 
                           request.form['price'], 
                           request.form['quantity'], 
                           )
        
            # Enviando para o banco
            db.session.add(newConsole)
            # Confirmando as alterações
            db.session.commit()
            return redirect(url_for('estoqueConsoles'))
        
        
            
        
        # fazendo um SELECT no banco (pegando todos os jogos da tabela)
        consolesestoque = Console.query.all()
        return render_template('estoqueConsoles.html', consolesestoque=consolesestoque)
    
    
    # rota de EDIÇÃO de jogos
    @app.route('/editGame/<int:id>', methods=['GET', 'POST'])
    def editGame(id):
        # busca o jogo pela id
        game = Game.query.get(id)
        
        # editando o jogo com as informações vinda do formulário 
        if request.method == "POST":
            # coletando as informações
            game.title = request.form['title']
            game.year = request.form['year']
            game.category = request.form['category']
            game.platform = request.form['platform']
            game.price = request.form['price']
            game.quantity = request.form['quantity']
            db.session.commit()
            
            return redirect(url_for('estoqueGames'))
                        
        return render_template('editGame.html', game=game)
    
        # rota de EDIÇÃO de consoles
    @app.route('/editConsole/<int:id>', methods=['GET', 'POST'])
    def editConsole(id):
        # busca o console pela id
        console = Console.query.get(id)
        
        # editando o jogo com as informações vinda do formulário 
        if request.method == "POST":
            # coletando as informações
            console.name = request.form['name']
            console.producer = request.form['producer']
            console.price = request.form['price']
            console.quantity = request.form['quantity']
            
            db.session.commit()
            
            return redirect(url_for('estoqueConsoles'))
                        
        return render_template('editConsole.html', console=console)