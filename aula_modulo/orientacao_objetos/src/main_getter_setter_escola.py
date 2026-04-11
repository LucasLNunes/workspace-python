from exemplo_escola_getter_setter import AlunoEscola


def main():
    aluno = AlunoEscola("Joana", 8.5)
    print(aluno)

    print("\nLendo propriedades (getter):")
    print("Nome:", aluno.nome)
    print("Nota:", aluno.nota)

    print("\nAtualizando propriedades (setter):")
    aluno.nome = "Joana Silva"
    aluno.nota = 9
    print(aluno)

    print("\nTentando atualizar com dado inválido:")
    try:
        aluno.nota = 15
    except Exception as erro:
        print("Erro capturado:", erro)


if __name__ == "__main__":
    main()
