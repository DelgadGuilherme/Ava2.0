from application import disciplina_lista

class DisciplinaDAO:
    def __init__(self):
        self._disciplina_lista = disciplina_lista

    def listar_todo(self):
        return self._disciplina_lista

    def listar_aula(self, disciplina):
        return disciplina.get_aula_lista
        