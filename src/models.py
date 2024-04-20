
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorite", back_populates="user", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    __tablename__ = "Favorites"
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("Character.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("Planet.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) 
    user = db.relationship("User", back_populates="favorites")
    favorite_character = db.relationship("Character", foreign_keys=[character_id])
    favorite_planet = db.relationship("Planets", foreign_keys=[planet_id])


class Character(db.Model):
    __tablename__ = "Character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(400))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


class Planets(db.Model):
    __tablename__ = "Planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(400))
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
