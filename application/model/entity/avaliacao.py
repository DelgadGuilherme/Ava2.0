class Avaliacao:
    def __init__(self, titulo, nota, data_entrega):
        self._titulo = titulo
        self._nota = nota
        self._data_entraga = data_entrega

    def get_titulo(self):
        return self._titulo

    def get_nota(self):
        return self._nota

    def get_data_entre(self):
        return self._data_entraga