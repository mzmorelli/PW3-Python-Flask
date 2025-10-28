from flask import Flask, render_template
import pymysql.cursors
from models.database import db

from controllers import routes
# carregando o flask na variável app

# importando o PyMySQL
import pymysql

app = Flask(__name__, template_folder='views')

# define o nome do banco de dados
DB_NAME = 'games'
app.config['DATABASE_NAME'] = DB_NAME

# passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'


routes.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    # conectando ao MysSQL e criando o banco de daods com suas ta belas
    
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor
                           )
    
    try:
        with conn.cursor() as cursor:
            # executando uma query 
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    except Exception as e:
        print(f"Erro ao criar o banco: {e}")
        
    finally:
        conn.close()
        
    # criando as tabelas 
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()

    # iniciando o servidor no localhost na porta 5000, modo de depuração ativado
    app.run(host='0.0.0.0', port=5000, debug=True)



# BIBLIOTECAS:  

# flask-sqlalchemy -> auxilia na criação dos models e fornece métodos pra manipular o BD
    # .findOne() -> método equivalente uma query SELECT
    # .create() -> método equivalente ao INSERT INTO
    # .delete() -> método equivalente ao DELETE
    # .update() -> método equivalente ao UPDATE
    
# pymysql -> permite conectar a aplicação Flask ao banco MySQL

# mysqlclient -> driver de conexão