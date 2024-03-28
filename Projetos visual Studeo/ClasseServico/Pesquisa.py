

class Pessquisa():
    def __init__(self, id, matricula, frota, placa):
        self.id = id
        self.matricula = matricula
        self.frota = frota
        self.placa = placa



    def PesquisaId(self, id):
        resultadoId = """SELECT * FROM VEICULO.ID_VEICULO"""

    def PesquisaMatricula(self, matricula):
        resultadoMatricula = """SELECT * FROM MOTORISTA.NR_MATRICULA"""


    def PesquisaId(self, frota):
        resultadoFrota = """SELECT * FROM VEICULO.FROTA"""

    def PesquisaId(self, placa):
        resultadoPlaca = """SELECT * FROM VEICULO.ID_PLACA"""