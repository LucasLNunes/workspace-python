# src/universidade/disciplina.py
from .conteudo_ministrado import ConteudoMinistrado
from .professor import Professor


class Disciplina:
    def __init__(self, nome, carga_horaria=60, professor=None):
        self.__nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor
        self.__conteudos_ministrados = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        if carga_horaria > 0:
            self.__carga_horaria = carga_horaria
        else:
            self.__carga_horaria = -1

    @property
    def professor(self):
        return self.__professor
    
    @professor.setter
    def professor(self, professor):
        if professor is not None and not issubclass(type(professor), Professor):
            raise TypeError("parâmetro professor deve derivar da classe Professor")
        self.__professor = professor

    def adicionar_conteudo_ministrado(self, descricao, carga_horaria):
        conteudo = ConteudoMinistrado(descricao, carga_horaria)
        self.__conteudos_ministrados.append(conteudo)

    def exibir_informacoes(self):
        print("Disciplina:", self.__nome)
        print("Carga Horária:", self.__carga_horaria)

        if self.__professor is not None:
            print("Professor Responsável:", self.__professor.nome)
        else:
            print("Disciplina sem professor alocado")
        
        print("Conteúdos Ministrados:")
        for cont in self.__conteudos_ministrados:
            print(f"\t-> id: {cont.id} - {cont.descricao} ({cont.carga_horaria} hora(s))")