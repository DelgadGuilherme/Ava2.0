from flask import Flask
import os

template_folder = os.path.abspath('application/view/templates')
static_folder = os.path.abspath('application/view/static')

app = Flask(__name__,template_folder = template_folder, static_folder = static_folder)


from application.model.entity.disciplina import Disciplina
from application.model.entity.aula import Aula
from application.model.entity.prova import Prova
from application.model.entity.trabalho import Trabalho


disciplina1 = Disciplina(1, "Legislação Aplicada a informatica", "Maria Fernada Ricci", "19:00 - 22:15", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 5, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de LAI"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de LAI"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de LAI"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de LAI"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de LAI"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de LAI"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de LAI"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de LAI"),
])

disciplina2 = Disciplina(2, "Laboratorio de programaçao de interface", "Tassio Auad", "19:00 - 22:15", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 5, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de LPI"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de LPI"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de LPI"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de LPI"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de LPI"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de LPI"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de LPI"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de LPI"),
    ])

disciplina3 = Disciplina(3, "Modelagem de banco de dados", "Anrafel", "19:00 - 22:15", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 3, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de MBD"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de MBD"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de MBD"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de MBD"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de MBD"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de MBD"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de MBD"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de MBD"),
    ])
    
disciplina4 = Disciplina(4, "OLHA NOME DEPOIS", "Felipe", "19:00 - 22:15", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 5, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de LAI"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de LAI"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de LAI"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de LAI"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de LAI"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de LAI"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de LAI"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de LAI"),
    ])

disciplina5 = Disciplina(5, "Gestão estrategica de pessoas", "Claudenir", "19:00 - 22:15", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 6, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de GEP"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de GEP"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de GEP"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de GEP"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de GEP"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de GEP"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de GEP"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de GEP"),
    ])
disciplina6 = Disciplina(6, "Gestão ambiental", "Cleber", "09:00 - 10:30", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 6, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de GA"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de GA"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de GA"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de GA"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de GA"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de GA"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de GA"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de GA"),
    ])
disciplina7 = Disciplina(7, "Empreendedorismo e inovação", "Marco Antonio", "10:30 - 12:00", 
[
    Trabalho('Trabalho 1 - P1', 2, "07/09/2020"),
    Trabalho('Trabalho 2 - P2', 2, "07/09/2020")
], 8, 
[
    Trabalho('Prova 1 - P1', 8, "07/09/2020"),
    Trabalho('Prova 2 - P2', 8, "07/09/2020")
],
[
    Aula(1,"Aula 1", "Introdução a materia"),
    Aula(2,"Aula 2", "Este é o titulo da aula 2 de EI"),
    Aula(3,"Aula 3", "Este é o titulo da aula 3 de EI"),
    Aula(4,"Aula 4", "Este é o titulo da aula 4 de EI"),
    Aula(5,"Aula 5", "Este é o titulo da aula 5 de EI"),
    Aula(6,"Aula 6", "Este é o titulo da aula 6 de EI"),
    Aula(7,"Aula 7", "Este é o titulo da aula 7 de EI"),
    Aula(8,"Aula 8", "Este é o titulo da aula 8 de EI"),
    Aula(9,"Aula 9", "Este é o titulo da aula 9 de EI"),
    ])

disciplina_lista = [disciplina1,disciplina2,disciplina3,disciplina4,disciplina5,disciplina6,disciplina7]


from application.controller import index_controller
from application.controller import disciplina_controller