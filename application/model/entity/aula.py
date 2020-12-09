class Aula:
    def __init__(self, id, numero, titulo):
        self._id = id
        self._numero = numero
        self._titulo = titulo

    def get_id(self):
        return self._id

    def get_numero(self):
        return self._numero

    def get_titulo(self):
        return self._titulo