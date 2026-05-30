from aluno import Aluno


def test_media_correta():
    aluno = Aluno("Maria")

    aluno.adicionar_nota(8)
    aluno.adicionar_nota(6)

    assert aluno.calcular_media() == 7


def test_nota_invalida():
    aluno = Aluno("João")

    try:
        aluno.adicionar_nota(15)
        assert False
    except ValueError:
        assert True


def test_aprovacao():
    aluno = Aluno("Carlos")

    aluno.adicionar_nota(9)
    aluno.adicionar_nota(8)

    assert aluno.verificar_situacao() == "Aprovado"


def test_recuperacao():
    aluno = Aluno("Ana")

    aluno.adicionar_nota(5)
    aluno.adicionar_nota(6)

    assert aluno.verificar_situacao() == "Recuperação"


def test_reprovacao():
    aluno = Aluno("Pedro")

    aluno.adicionar_nota(2)
    aluno.adicionar_nota(4)

    assert aluno.verificar_situacao() == "Reprovado"
