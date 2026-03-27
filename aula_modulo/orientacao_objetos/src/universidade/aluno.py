from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

        
