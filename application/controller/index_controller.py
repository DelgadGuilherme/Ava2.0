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
    trabalhos_provas_lista = []

    for disciplina in disciplina_lista:
        provas += disciplina.get_avaliacao_qnt()
        foruns += disciplina.get_forum()
        trabalhos += disciplina.get_trabalho_qnt()
        for trabalho in disciplina.get_trabalho_lista():
            trabalhos_provas_lista.append(trabalho)

        for avaliacao in disciplina.get_avaliacao_lista():
            trabalhos_provas_lista.append(avaliacao)

   
    lembrete_lista = [trabalhos_provas_lista[0], trabalhos_provas_lista[2], trabalhos_provas_lista[5]]

    

    return render_template('index.html', disciplina_lista = disciplina_lista, provas=provas, trabalhos=trabalhos, foruns=foruns, lembrete_lista=lembrete_lista )
    