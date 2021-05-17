# from fontColor import cor, sucesso, erro
import cores

def menu(titulo, opcoes):
    while True:
        print(cores.cor(f"\t{titulo.upper()}", "azul"))
        for i in range(len(opcoes)):
            print(cores.cor(f"[{i+1}] {opcoes[i]}", "ciano"))
        try:
            escolha = int(input("Escolha uma opcao: ")) - 1
        except ValueError:
            print(cores.erro("Por favor, insira apenas o numero da opção desejada"))
        except Exception as e:
            print(cores.erro(f"erro {e.__class__}"))
            print(cores.erro("um erro inesperado aconteceu."))
            return -1
        else:
            if escolha in range(len(opcoes)):
                return escolha
            print(cores.erro("Opção inválida! Escolha um dos valores apresentados na tela."))
