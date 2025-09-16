from sistema import Pesquisador, Participante, OrgaoAmbiental, BancoDeDados, AnalistaDeDados

def menu():
    print("\n=== Sistema de Pesquisa Clínica e Produção Farmacêutica ===")
    print("1 - Criar Relatório Científico")
    print("2 - Gerenciar Participantes")
    print("3 - Inserir Resultado de Pesquisa")
    print("4 - Inserir Impacto Ambiental")
    print("5 - Listar Banco de Dados")
    print("6 - Análise de Dados")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    pesquisador = Pesquisador("Dr. João")
    orgao = OrgaoAmbiental("MMA")
    banco = BancoDeDados()
    analista = AnalistaDeDados("Maria")
    participantes = []

    while True:
        opcao = menu()

        if opcao == "1":
            relatorio = pesquisador.relatorio_cientifico()
            banco.salvar(relatorio)
            print("✅ Relatório criado e salvo.")

        elif opcao == "2":
            nome = input("Nome do participante: ")
            idade = int(input("Idade do participante: "))
            participantes.append(Participante(nome, idade))
            dado = pesquisador.gerenciamento_pessoas(participantes)
            banco.salvar(dado)
            print("✅ Participante adicionado.")

        elif opcao == "3":
            resultado = input("Digite o resultado da pesquisa: ")
            dado = pesquisador.resultado_pesquisa(resultado)
            banco.salvar(dado)
            print("✅ Resultado salvo.")

        elif opcao == "4":
            descricao = input("Descreva o impacto ambiental: ")
            impacto = orgao.impacto_ambiental(descricao)
            banco.salvar(impacto)
            print("✅ Impacto ambiental registrado.")

        elif opcao == "5":
            print("\n=== Banco de Dados ===")
            for dado in banco.listar_dados():
                print(f"- {dado}")

        elif opcao == "6":
            print(analista.analisar(banco))

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
