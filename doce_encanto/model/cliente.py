from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    whats = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"<Cliente {self.nome}>"

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'whats': self.whats
        }