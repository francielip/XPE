from flask import Flask
from controller.cliente_controller import cliente_bp
from model.cliente import db

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Registra o Blueprint do cliente (Controlador)
app.register_blueprint(cliente_bp, url_prefix='/clientes')

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)