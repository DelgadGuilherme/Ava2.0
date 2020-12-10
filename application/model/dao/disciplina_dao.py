from application import disciplina_lista

class DisciplinaDAO:
    def __init__(self):
        self._disciplina_lista = disciplina_lista

    def listar_todo(self):
        return self._disciplina_lista

    def listar_aula(self, disciplina):
        return disciplina.get_aula_lista
        
    def buscar_por_id(self, id):
        for i in range(0, len(self._disciplina_lista)):
            if self._disciplina_lista[i].get_id() == int(id):
                return self._disciplina_lista[i] 
        return None
