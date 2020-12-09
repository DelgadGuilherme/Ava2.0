from flask import render_template, request
from application import app 
from application.model.dao.disciplina_dao import DisciplinaDAO


@app.route('/')
@app.route('/home')
def home():
    disciplina_dao = DisciplinaDAO()
    disciplina_lista = disciplina_dao.listar_todo()

    provas = 0
    trabalhos = 0
    foruns = 0

    for disciplina in disciplina_lista:
        provas += disciplina.get_avaliacao()
        foruns += disciplina.get_forum()
        trabalhos += disciplina.get_trabalho()

    return render_template('index.html', disciplina_lista = disciplina_lista, provas=provas, trabalhos=trabalhos, foruns=foruns)
    