from src.leilao.excecoes import LanceInvalido
import unittest
import pytest

from src.leilao.dominio import Lance, Leilao, Usuario


class TestLeilao(unittest.TestCase):

    def setUp(self):
        self.user1 = Usuario('Júlio', 500.0)
        self.user2 = Usuario('Carlos', 500.0)
        self.lance_julio = Lance(self.user1, 250.0)
        self.lance_carlos = Lance(self.user2, 300.0)

        self.leilao = Leilao("celular")

    def test_entrada_2_lances_ordem_crescente_saida_maior_e_menor_valor_corretos(self):

        self.leilao.propoe(self.lance_julio)
        self.leilao.propoe(self.lance_carlos)

        self.assertEqual(250.0, self.leilao.menor_lance)
        self.assertEqual(300.0, self.leilao.maior_lance)

    def test_entrada_2_lances_ordem_decrescente_saida_ValueError(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_carlos)
            self.leilao.propoe(self.lance_julio)

    def test_entrada_1_lance_saida_maior_e_menor_valor_iguais(self):

        self.leilao.propoe(self.lance_julio)

        self.assertEqual(250.0, self.leilao.menor_lance)
        self.assertEqual(250.0, self.leilao.maior_lance)

    def test_entrada_3_lances_saida_maior_e_menor_valor_corretos(self):

        outro_lance_carlos = Lance(self.user2, 200.0)
        self.leilao.propoe(outro_lance_carlos)
        self.leilao.propoe(self.lance_julio)
        self.leilao.propoe(self.lance_carlos)

        self.assertEqual(200.0, self.leilao.menor_lance)
        self.assertEqual(300.0, self.leilao.maior_lance)

    # se o leilao nao tiver lance, deve permitir um lance

    def test_entrada_1_lance_leilao_vazio_saida_tamanho_leilao_igual_a_1(self):

        self.leilao.propoe(self.lance_julio)

        self.assertEqual(1, len(self.leilao.lances))

    # se o ultimo usuario for diferente deve permitir lance

    def test_entrada_2_lance_usuarios_diferentes_saida_tamanho_leilao_igual_a_2(self):

        self.leilao.propoe(self.lance_julio)
        self.leilao.propoe(self.lance_carlos)

        self.assertEqual(2, len(self.leilao.lances))

    # se o ultimo usuario for igual não deve permitir

    def test_entrada_2_lance_usuarios_iguais_saida_tamanho_leilao_igual_a_1(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_carlos)
            outro_lance_carlos = Lance(self.user2, 200.0)
            self.leilao.propoe(outro_lance_carlos)
        self.assertEqual(1, len(self.leilao.lances))


if __name__ == '__main__':
    unittest.main()
