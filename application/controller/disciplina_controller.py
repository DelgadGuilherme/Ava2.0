from flask import render_template, request
from application import app
from application.model.dao.disciplina_dao import DisciplinaDAO



@app.route('/disciplina/<disciplina_id>')
def disciplina(disciplina_id):
    disciplina_dao =  DisciplinaDAO()
    disciplina = disciplina_dao.buscar_por_id(disciplina_id)
    aula_lista = disciplina.get_aula_lista()

    trabalhos_provas_lista = []
    for trabalho in disciplina.get_trabalho_lista():
        trabalhos_provas_lista.append(trabalho)

    for avaliacao in disciplina.get_avaliacao_lista():
        trabalhos_provas_lista.append(avaliacao)

    return render_template('disciplina.html', disciplina=disciplina, aula_lista = aula_lista, lembretes_lista = trabalhos_provas_lista )
    