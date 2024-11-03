from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Professor, Turma, Aluno
from .forms import ProfessorForm, TurmaForm, AlunoForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')

# Professores
@main.route('/professores', methods=['GET', 'POST'])
def listar_professores():
    professores = Professor.query.all()
    form = ProfessorForm()

    if form.validate_on_submit():
        novo_professor = Professor(
            nome=form.nome.data,
            idade=form.idade.data,
            materia=form.materia.data,
            observacoes=form.observacoes.data
        )
        db.session.add(novo_professor)
        db.session.commit()
        flash('Professor adicionado com sucesso!', 'success')
        return redirect(url_for('main.listar_professores'))

    return render_template('professor.html', professores=professores, form=form)

@main.route('/professores/edit/<int:id>', methods=['GET', 'POST'])
def editar_professor(id):
    professor = Professor.query.get_or_404(id)
    form = ProfessorForm(obj=professor)

    if form.validate_on_submit():
        professor.nome = form.nome.data
        professor.idade = form.idade.data
        professor.materia = form.materia.data
        professor.observacoes = form.observacoes.data
        db.session.commit()
        flash('Professor editado com sucesso!', 'success')
        return redirect(url_for('main.listar_professores'))

    return render_template('editar_professor.html', form=form)

@main.route('/professores/delete/<int:id>', methods=['POST'])
def deletar_professor(id):
    professor = Professor.query.get_or_404(id)
    db.session.delete(professor)
    db.session.commit()
    flash('Professor excluído com sucesso!', 'success')
    return redirect(url_for('main.listar_professores'))

# Turmas
@main.route('/turmas', methods=['GET', 'POST'])
def listar_turmas():
    turmas = Turma.query.all()
    form = TurmaForm()

    form.professor_id.choices = [(p.id, p.nome) for p in Professor.query.all()]

    if form.validate_on_submit():
        nova_turma = Turma(
            descricao=form.descricao.data,
            professor_id=form.professor_id.data
        )
        db.session.add(nova_turma)
        db.session.commit()
        flash('Turma adicionada com sucesso!', 'success')
        return redirect(url_for('main.listar_turmas'))

    return render_template('turma.html', turmas=turmas, form=form)

@main.route('/turmas/edit/<int:id>', methods=['GET', 'POST'])
def editar_turma(id):
    turma = Turma.query.get_or_404(id)
    form = TurmaForm(obj=turma)

    form.professor_id.choices = [(p.id, p.nome) for p in Professor.query.all()]

    if form.validate_on_submit():
        turma.descricao = form.descricao.data
        turma.professor_id = form.professor_id.data
        db.session.commit()
        flash('Turma editada com sucesso!', 'success')
        return redirect(url_for('main.listar_turmas'))

    return render_template('editar_turma.html', form=form)

@main.route('/turmas/delete/<int:id>', methods=['POST'])
def deletar_turma(id):
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    flash('Turma excluída com sucesso!', 'success')
    return redirect(url_for('main.listar_turmas'))

# Alunos
@main.route('/alunos', methods=['GET', 'POST'])
def listar_alunos():
    alunos = Aluno.query.all()
    form = AlunoForm()

    form.turma_id.choices = [(t.id, t.descricao) for t in Turma.query.all()]

    if form.validate_on_submit():
        nova_aluno = Aluno(
            nome=form.nome.data,
            idade=form.idade.data,
            turma_id=form.turma_id.data,
            data_nascimento=form.data_nascimento.data,
            nota_primeiro_semestre=form.nota_primeiro_semestre.data,
            nota_segundo_semestre=form.nota_segundo_semestre.data,
            media_final=(form.nota_primeiro_semestre.data + form.nota_segundo_semestre.data) / 2
        )
        db.session.add(nova_aluno)
        db.session.commit()
        flash('Aluno adicionado com sucesso!', 'success')
        return redirect(url_for('main.listar_alunos'))

    return render_template('aluno.html', alunos=alunos, form=form)

@main.route('/alunos/edit/<int:id>', methods=['GET', 'POST'])
def editar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    form = AlunoForm(obj=aluno)

    form.turma_id.choices = [(t.id, t.descricao) for t in Turma.query.all()]

    if form.validate_on_submit():
        aluno.nome = form.nome.data
        aluno.idade = form.idade.data
        aluno.turma_id = form.turma_id.data
        aluno.data_nascimento = form.data_nascimento.data
        aluno.nota_primeiro_semestre = form.nota_primeiro_semestre.data
        aluno.nota_segundo_semestre = form.nota_segundo_semestre.data
        aluno.media_final = (form.nota_primeiro_semestre.data + form.nota_segundo_semestre.data) / 2
        db.session.commit()
        flash('Aluno editado com sucesso!', 'success')
        return redirect(url_for('main.listar_alunos'))

    return render_template('editar_aluno.html', form=form)

@main.route('/alunos/delete/<int:id>', methods=['POST'])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    flash('Aluno excluído com sucesso!', 'success')
    return redirect(url_for('main.listar_alunos'))