from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, Optional, ValidationError
from smartMoving.models import User

class FormularioRegistro(Form):
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=4, max=20, message='O nome de usuário deve conter entre 4 e 20 caracteres!')])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=30, message='A senha deve conter entre 8 e 30 caracteres!')])
    confirm_password = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('password', message='As senhas devem ser iguais!')])
    submit = SubmitField('Completar cadastro')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Esse nome de usuário já está sendo utilizado! Por favor, escolha outro.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Esse e-mail já está sendo utilizado! Por favor, escolha outro.')

class FormularioLogin(Form):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar de mim')
    submit = SubmitField('Login')