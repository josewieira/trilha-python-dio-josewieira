from datetime import datetime

# Constantes
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3

# Estado inicial
saldo = 0
extrato = []
numero_saques = 0

# Menu de operações
menu = """
=============== MENU ===============

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Funções
def registrar_operacao(tipo, valor):
    """Adiciona uma linha formatada ao extrato com data/hora."""
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    operacao = f"{timestamp} - {tipo}: R$ {valor:.2f}"
    extrato.append(operacao)

def depositar():
    global saldo
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            registrar_operacao("Depósito", valor)
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. Deposite apenas valores positivos.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

def sacar():
    global saldo, numero_saques
    try:
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O saque excede o limite de R$ {LIMITE_SAQUE}.")
        elif excedeu_saques:
            print("Operação falhou! Limite diário de saques atingido.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            registrar_operacao("Saque", valor)
            print("Saque realizado com sucesso.")
        else:
            print("Valor inválido. Saque apenas valores positivos.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

def mostrar_extrato():
    print("\n================ EXTRATO ================\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

# Loop principal
while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        mostrar_extrato()
    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema. Até a próxima!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
