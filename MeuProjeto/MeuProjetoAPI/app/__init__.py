from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

# Inicialização das extensões
bootstrap = Bootstrap()
csrf = CSRFProtect()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0000'  #Proteger os dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'  #URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Inicializa as extensões com a aplicação
    bootstrap.init_app(app)
    csrf.init_app(app)
    db.init_app(app)

    #Importa e registra o blueprint
    from .routes import main
    app.register_blueprint(main)

    #Inicializa o banco de dados
    with app.app_context():
        db.create_all()

    return app