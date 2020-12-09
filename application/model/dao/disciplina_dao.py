from application.model.entity.disciplina import Disciplina
from application import disciplina_list

class DisciplinaDAO:
    def __init__(self):
        self.disciplina_list = disciplina_list

    def listar_todo(self):
        return self.disciplina_list

    def listar_aula(self, disciplina):
        return disciplina.get_aula_lista
        