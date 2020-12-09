class Disciplina:

    def __init__(self, id, nome, professor, horario, trabalho, forum, avaliacao):
        self._id = id
        self._nome = nome
        self._professor = professor
        self._horario = horario
        self._trabalho = trabalho
        self._forum = forum
        self._avalicao = avalicao
        self._aula_lista = []
                
    def get_nome(self):
        return self._nome

    def get_professor(self):
        return self._professor

    def get_horario(self):
        return self._horario

    def get_trabalho(self):
        return self._trabalho

    def get_forum(self):
        return self._forum

    def get_avaliacao(self):
        return self._avalicao