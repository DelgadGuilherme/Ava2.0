from application.model.entity.avaliacao import Avaliacao
class Trabalho(Avaliacao):
    def __init__(self, titulo, nota, data_entrega):
        Avaliacao.__init__(self,titulo,nota,data_entrega)