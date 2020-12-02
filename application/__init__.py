from flask import Flask
import os

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)

from application.controller.index_controller import home

from application.model.entity.disciplina import Disciplina
from application.model.entity.periodo import Periodo

disciplina1 = Disciplina(1, "Legislação Aplicada a informatica", "Maria Fernada Ricci", "19:00 - 22:15", 2, 5, 2)
disciplina2 = Disciplina(2, "Laboratorio de programaçao de interface", "Tassio Auad", "19:00 - 22:15", 2, 9, 2)
disciplina3 = Disciplina(3, "Modelagem de banco de dados", "Anrafel", "19:00 - 22:15", 2, 3, 2)
disciplina4 = Disciplina(4, "OLHA NOME DEPOIS", "Felipe", "19:00 - 22:15", 2, 5, 2)
disciplina5 = Disciplina(5, "Gestão estrategica de pessoas", "Claudenir", "19:00 - 22:15", 2, 6, 2)
disciplina6 = Disciplina(6, "Gestão ambiental", "Cleber", "8:00 - 10:30", 2, 10, 2)
disciplina7 = Disciplina(7, "Empreendedorismo e inovação", "Marco Antonio", "10:30 - 12:00", 2, 5, 2)

perido1 = Periodo(4, "4º",[disciplina1, disciplina2, disciplina3, disciplina4, disciplina5, disciplina6, disciplina7])