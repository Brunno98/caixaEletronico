import cores

CAMINHO = "./registros.txt"

def escreveArquivo(banco, nome, conta, acao, valor, data):
    try:
        arquivo = open(CAMINHO, 'at')
        arquivo.write(f"{banco};{nome};{conta};{acao};{valor};{data}\n")
    except:
        print(cores.erro("nao foi possivel abrir o arquivo."))
    finally:
        arquivo.close() 

def relatorioDiario(data):
    try:
        arquivo = open(CAMINHO, 'rt')
    except FileNotFoundError:
        print(cores.aviso("Não há registro de operações realizadas."))
    except Exception as e:
        print(cores.erro(f"Ocorreu um erro inesperado. Erro: {e.__class__}"))
    else:
        total = 0
        linha = arquivo.readline()
        while linha:
            linha = linha.split(';')
            if linha[3] == "saque" and linha[5].replace('\n', '') == data:
                total += float(linha[4])
            linha = arquivo.readline()
        arquivo.close()
        return total


def registroDeTodosOsDias():
    try:
        arquivo = open(CAMINHO, 'rt')
    except FileNotFoundError:
        print(cores.aviso("Não há registro de operações realizadas."))
    except Exception as e:
        print(cores.erro(f"Ocorreu um erro inesperado. Erro: {e.__class__}"))
    else:
        dias = []
        linha = arquivo.readline()
        while linha:
            linha = linha.split(';')
            data = linha[5].replace('\n', '')
            if data not in dias:
                dias.append(linha[5].replace('\n', ''))
            linha = arquivo.readline()
        arquivo.close()
        for dia in dias:
            print(f"Relatorio de saque diario no dia {dia}: R${relatorioDiario(dia):.2f}")


def sacar(banco, nome, conta, valor, data):
    try:
        escreveArquivo(banco, nome, conta, "saque", valor, data)
        print(cores.sucesso("Saque efetuado com sucesso."))
    except:
        print(cores.erro("Não foi possivel realizar o saque."))

def depositar(banco, nome, conta, valor, data):
    try:
        escreveArquivo(banco, nome, conta, "deposito", valor, data)
        print(cores.sucesso("Depósito efetuado com sucesso."))
    except:
        print(cores.erro("Não foi possivel realizar o depósito."))
