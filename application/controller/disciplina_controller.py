from flask import render_template, request
from application import app 

@app.route('/disciplina/<disciplina_id>')
def disciplina(disciplina_id):

    return render_template('disciplina.html')
    