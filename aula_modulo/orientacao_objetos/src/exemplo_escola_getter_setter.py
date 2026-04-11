class AlunoEscola:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    @property
    def nome(self):
        print("Getter de nome foi chamado")
        return self.__nome

    @nome.setter
    def nome(self, valor):
        print("Setter de nome foi chamado")
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome deve ser um texto não vazio.")
        self.__nome = valor.strip()

    @property
    def nota(self):
        print("Getter de nota foi chamado")
        return self.__nota

    @nota.setter
    def nota(self, valor):
        print("Setter de nota foi chamado")
        if not isinstance(valor, (int, float)):
            raise TypeError("Nota deve ser número.")
        if valor < 0 or valor > 10:
            raise ValueError("Nota deve estar entre 0 e 10.")
        self.__nota = float(valor)

    def __str__(self):
        return f"Aluno: {self.__nome} | Nota: {self.__nota:.1f}"
