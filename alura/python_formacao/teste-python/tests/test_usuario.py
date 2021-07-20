import pytest
from src.leilao.dominio import Leilao, Usuario, LanceInvalido


@pytest.fixture
def vini():
    return Usuario("Vini", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Celular")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0


def test_deve_permitir_se_valor_do_lance_for_menor_que_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0


def test_deve_permitir_se_valor_do_lance_for_igual_ao_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0


def test_nao_deve_permitir_se_valor_do_lance_for_maior_que_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    with pytest.raises(LanceInvalido):

        vini.propoe_lance(leilao, 150.0)

        assert vini.carteira == 100.0
