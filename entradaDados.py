import cores

def inserirNome():
    try:
        nome = input("Digite seu nome: ").strip().title()
    except KeyboardInterrupt:
        print(cores.aviso("\nAção interronpida pelo usuário."))
        return None
    else:
        if not nome:
            return None
        return nome


def inserirConta():
    while True:
        try:
            conta = input("Digite o numero da conta: ").strip()
        except KeyboardInterrupt:
            print(cores.aviso("\nAção interrompida pelo usuário"))
            return None
        else:
            if not conta:
                return None
            if conta.replace('-', '').isdigit():
                return conta
            print(cores.erro("Numero de conta inválido! tente novamente."))


def inserirValor(texto):
    while True:
        try:
            valor = input(texto).replace(',', '.')
            valor = float(valor)
        except ValueError:
            print(cores.erro("Por favor, digite um valor válido."))
        except Exception as e:
            print("erro: ", e.__class__)
            print(cores.erro("Valor Inválido! Tente novamente."))
        else:
            if valor > 0:
                return valor
            print(cores.erro("O valor precisa ser maior que 0 (zero)."))