class Disciplina:

    def __init__(self, id, nome, professor, horario, trabalho_lista, forum, avaliacao_lista, aula_lista):
        self._id = id
        self._nome = nome
        self._professor = professor
        self._horario = horario
        self._trabalho_lista = trabalho_lista
        self._forum = forum
        self._avaliacao_lista = avaliacao_lista
        self._aula_lista = aula_lista
                
    def get_id(self):
        return self._id
        
    def get_nome(self):
        return self._nome

    def get_professor(self):
        return self._professor

    def get_horario(self):
        return self._horario

    def get_trabalho_lista(self):
        return self._trabalho_lista

    def get_trabalho_qnt(self):
        return len(self._trabalho_lista)

    def get_forum(self):
        return self._forum

    def get_avaliacao_lista(self):
        return self._avaliacao_lista

    def get_avaliacao_qnt(self):
        return len(self._avaliacao_lista)

    def get_aula_lista(self):
        return self._aula_lista