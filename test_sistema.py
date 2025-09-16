import unittest
from sistema import Pesquisador, Participante, OrgaoAmbiental, BancoDeDados, AnalistaDeDados


class TestSistema(unittest.TestCase):

    def setUp(self):
        self.pesquisador = Pesquisador("Dr. João")
        self.participantes = [Participante("Ana", 25), Participante("Carlos", 30)]
        self.orgao = OrgaoAmbiental("IBAMA")
        self.banco = BancoDeDados()
        self.analista = AnalistaDeDados("Maria")

    def test_relatorio_cientifico(self):
        texto = self.pesquisador.relatorio_cientifico()
        self.assertIn("Relatório científico elaborado", texto)

    def test_gerenciamento_pessoas(self):
        texto = self.pesquisador.gerenciamento_pessoas(self.participantes)
        self.assertIn("2 pessoas foram gerenciadas", texto)

    def test_resultado_pesquisa(self):
        resultado = self.pesquisador.resultado_pesquisa("Eficácia 90%")
        self.assertEqual(resultado, "Resultado da pesquisa: Eficácia 90%")

    def test_participante(self):
        p = Participante("João", 40)
        self.assertEqual(p.nome, "João")
        self.assertEqual(p.idade, 40)

    def test_impacto_ambiental(self):
        impacto = self.orgao.impacto_ambiental("Baixo impacto")
        self.assertIn("Baixo impacto", impacto)

    def test_banco_salvar_listar(self):
        self.banco.salvar("Dado 1")
        self.banco.salvar("Dado 2")
        dados = self.banco.listar_dados()
        self.assertEqual(len(dados), 2)
        self.assertIn("Dado 1", dados)

    def test_analista(self):
        self.banco.salvar("Teste")
        resultado = self.analista.analisar(self.banco)
        self.assertIn("1 registros", resultado)


if __name__ == "__main__":
    unittest.main()
