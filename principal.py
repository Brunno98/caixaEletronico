# Aluno: Brunno Santana Soares
# Matricula: 202002770317

import datetime
import cores
import registro
from exibicao import menu
from entradaDados import inserirNome, inserirConta, inserirValor


DATA = datetime.datetime.now()
HOJE = f"{DATA.day}/{DATA.month}/{DATA.year}"
BANCOS = ("Santander", "Banco do Brasil", "Caixa", "Bradesco", "Itaú")


banco = None
nome = None
conta = None

while True:
    print(cores.status(banco, f"Banco: {banco}"))
    print(cores.status(nome, f"Nome: {nome}"))
    print(cores.status(conta, f"Conta: {conta}"))
    escolha = menu(
        "Menu Principal",
        [
            "Escolher Banco",
            "Digitar Nome e Conta",
            "Sacar - Depositar",
            "Sair"
        ]
    )
    if escolha == 0:
        banco = BANCOS[menu("Opções de Bancos:", BANCOS)]
    elif escolha == 1:
        nome = inserirNome()
        conta = inserirConta()
    elif escolha == 2:
        if not banco:
            print(cores.aviso("É necessário informar o Banco antes de sacar ou depositar\n"))
        elif not nome or not conta:
            print(cores.aviso("É necessário inserir o nome e número da conta antes de sacar ou depositar\n"))
        else:
            operacao = menu(
                "Menu de saque e depósito",
                [
                    "Saque.",
                    "Depósito.",
                    "Sair."
                ]
            )
            if operacao == 0:
                valor = inserirValor("Valor a ser sacado: R$")
                registro.sacar(banco, nome, conta, valor, HOJE)
            elif operacao == 1:
                valor = inserirValor("Valor a ser depositado: R$")
                registro.depositar(banco, nome, conta, valor, HOJE)
            elif operacao == 2:
                print(cores.aviso("saindo..."))
    elif escolha == 3:
        print(cores.sucesso("Até logo. Tenha um bom dia!"))
        total = registro.relatorioDiario(HOJE)
        if total:
            print(f"Total sacado hoje ({HOJE}) foi: R${total:.2f}")
        registro.registroDeTodosOsDias()
        break
    else:
        print(cores.erro("Opção inválida! Tente Novamente"))