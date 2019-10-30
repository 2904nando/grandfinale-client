from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, Optional

class FormularioRegistro(Form):
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=4, max=20, message='O nome de usuário deve conter entre 4 e 20 caracteres!')])
    email = StringField('E-mail', validators=[DataRequired(), Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=30, message='A senha deve conter entre 8 e 30 caracteres!')])
    confirm_password = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('password', message='As senhas devem ser iguais!')])
    submit = SubmitField('Completar cadastro')

class FormularioLogin(Form):
    email = StringField('E-mail', validators=[DataRequired(),
                                              Email(message='E-mail inválido!')])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar de mim')
    submit = SubmitField('Login')