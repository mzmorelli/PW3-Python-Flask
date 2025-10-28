from flask_sqlalchemy import SQLAlchemy


# criar uma instância do sqlalchemy na variável
db = SQLAlchemy()

# criando o model (classe)
class Game(db.Model):
    # criando os atributos da tabela
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(150))
    year = db.Column(db.Integer)
    category = db.Column(db.String(150))
    platform = db.Column(db.String(150))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    def __init__(self, title, year, category, platform, price, quantity):
        self.title = title
        self.year = year
        self.category = category
        self.price = price
        self.platform = platform
        self.quantity = quantity
    
class Console(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150))
    producer = db.Column(db.String(150))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    
    # método construtor da classe do python
    def __init__(self, name, producer, price, quantity):
        self.name = name
        self.producer = producer
        self.price = price
        self.quantity = quantity
        
    