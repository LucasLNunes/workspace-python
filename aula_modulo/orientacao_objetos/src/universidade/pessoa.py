# src/universidade/pessoa.py
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self) -> str:
        return f"{self.nome} {self._formatar_cpf()}"

    def __lt__(self, other) -> bool:
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.nome < other.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido")
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if self.__validar_cpf(cpf):
            self.__cpf = cpf
        else:
            raise ValueError("CPF Inválido")
        
    def __validar_cpf(self, cpf_teste):
        if not isinstance(cpf_teste, int):
            return False
        if cpf_teste < 0:
            return False
        cpf_str = str(cpf_teste)
        if len(cpf_str) != 11:
            return False
        if len(set(cpf_str)) == 1:
            return False

        somatorio_valida_ultimo = 0
        somatorio_valida_penultimo = 0

        ultimo = cpf_teste % 10
        cpf_teste //= 10
        penultimo = cpf_teste % 10
        cpf_teste //= 10

        somatorio_valida_ultimo = penultimo * 2
        for i in range(2, 12):
            modulo = cpf_teste % 10
            cpf_teste //= 10
            somatorio_valida_penultimo += modulo * i
            somatorio_valida_ultimo += modulo * (i + 1)

        modulo = somatorio_valida_penultimo % 11
        if modulo < 2:
            if penultimo != 0:
                return False
        else:
            if penultimo != 11 - modulo:
                return False

        modulo = somatorio_valida_ultimo % 11
        if modulo < 2:
            if ultimo != 0:
                return False
        else:
            if ultimo != 11 - modulo:
                return False

        return True

    def _formatar_cpf(self) -> str:
        cpf_str = str(self.__cpf)
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

    def __str__(self) -> str:
        verificador = self.cpf%100
        atual = self.cpf//100
        terc = atual%1000
        atual = atual//1000
        seg = atual%1000
        prim = atual//1000
        return f"{self.nome} {prim:03d}.{seg:03d}.{terc:03d}-{verificador:02d}"
