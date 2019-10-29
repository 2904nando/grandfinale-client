from smartMoving import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    dt_nasc = db.Column(db.DateTime)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    permissoes = db.relationship('Permissao_Usuario', backref='usuario', lazy=True)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')'"


class Permissao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    usuarios = db.relationship('Permissao_Usuario', backref="permissao", lazy=True)

    def __repr__(self):
        return f"Permissão('{self.name}')"

class Permissao_Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissao.id'), nullable=False)

    def __repr__(self):
        return f"Permissão_Usuario('{self.user_id}, {self.permission_id}')"