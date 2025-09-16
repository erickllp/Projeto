"""
Sistema de Pesquisa Clínica e Produção Farmacêutica
Cada método possui análise de complexidade Big-O.
"""

class Pesquisador:
    def __init__(self, nome):
        self.nome = nome

    def relatorio_cientifico(self):
        """
        Complexidade: O(1)
        """
        return f"Relatório científico elaborado por {self.nome}"

    def gerenciamento_pessoas(self, participantes):
        """
        Complexidade: O(1) - len(lista) em Python é constante
        """
        return f"{len(participantes)} pessoas foram gerenciadas pelo pesquisador {self.nome}"

    def resultado_pesquisa(self, resultados):
        """
        Complexidade: O(1)
        """
        return f"Resultado da pesquisa: {resultados}"


class Participante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class OrgaoAmbiental:
    def __init__(self, nome):
        self.nome = nome

    def impacto_ambiental(self, descricao):
        """
        Complexidade: O(1)
        """
        return f"Órgão {self.nome} avaliou o impacto ambiental: {descricao}"


class BancoDeDados:
    def __init__(self):
        self.dados = []

    def salvar(self, info):
        """
        Complexidade: O(1) - append
        """
        self.dados.append(info)
        return True

    def listar_dados(self):
        """
        Complexidade: O(n) - percorre a lista
        """
        return self.dados


class AnalistaDeDados:
    def __init__(self, nome):
        self.nome = nome

    def analisar(self, banco):
        """
        Complexidade: O(1) - len(lista)
        """
        return f"Analista {self.nome} encontrou {len(banco.dados)} registros no banco de dados."
