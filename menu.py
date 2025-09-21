from sistema import Pesquisador, Participante, OrgaoAmbiental, BancoDeDados, AnalistaDeDados
import random


def menu():
    print("\n=== Sistema de Pesquisa Clínica e Produção Farmacêutica ===")
    print("1 - Parciente")
    print("2 - Pesquisador")
    print("0 - Sair")
    return input("Escolha uma opção: ")
    print("")
    print("-------------------------------------------")
    print("")

def main():
    pesquisador = Pesquisador("Dr. João")
    orgao = OrgaoAmbiental("MMA")
    banco = BancoDeDados()
    analista = AnalistaDeDados("Maria")
    participantes = []

    while True:
        opcao = menu()

        if opcao == "1":
            print("o você esta procurando?")
            print("1 - criar cadastro")
            print("2 - Verificar resultado")
            print("0 - voltar para tela inical")
            paciente = input("escolha: ")
            if paciente =="1":
                nome = input("Nome do participante: ")
                idade = int(input("Idade do participante: "))
                participantes.append(Participante(nome, idade))
                dado = pesquisador.gerenciamento_pessoas(participantes)
                banco.salvar(dado)
                print("✅ Participante adicionado.")
            elif paciente == "2":
                eficacia = random.uniform(0, 100)
                print(f"{eficacia:.2f}")
                if eficacia > 80:
                    print(f"✅ Eficácia aprovada com {eficacia:.2f}%")
                    dado = pesquisador.resultado_pesquisa(f"{eficacia:.2f}%")
                    banco.salvar(dado)
                else:
                    print("Eficacia insuficiente")    
        elif opcao == "2":
            senha = 123
            acesso = input("ambiente restrito, informe senha para continuar: ")
            if acesso == senha:
                print("Acesso permitido")
                print("o que deseja acessar: ")  #criar opcões de escolha caso informe a senha
                                                 #escolhas = relatorios, ambiente, resultados       
            else:
                print("acesso negado")      #voltar para inicio, ou encerrar code
            


        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
