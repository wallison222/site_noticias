from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from . import db

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
# Compare this snippet from app/auth.py: