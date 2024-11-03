from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, SelectField, DateField, TextAreaField, BooleanField
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Optional

class ProfessorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[Optional()])
    materia = StringField('Matéria', validators=[Optional()])
    email = StringField('Email', validators=[Email(), Optional()])
    observacoes = TextAreaField('Observações', validators=[Optional()])

class TurmaForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired()])
    professor_id = SelectField('Professor', coerce=int)

class AlunoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    turma_id = SelectField('Turma', coerce=int)
    data_nascimento = DateField('Data de Nascimento', format='%Y-%m-%d')
    nota_primeiro_semestre = DecimalField('Nota do Primeiro Semestre', places=2)
    nota_segundo_semestre = DecimalField('Nota do Segundo Semestre', places=2)
    submit = SubmitField('Adicionar Aluno')