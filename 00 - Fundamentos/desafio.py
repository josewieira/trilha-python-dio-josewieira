from datetime import datetime 

 

# ======== CONSTANTES ======== 

LIMITE_SAQUE = 500 

LIMITE_SAQUES_DIARIOS = 3 

 

# ======== ESTADOS GLOBAIS ======== 

usuarios = [] 

contas = [] 

 

# ======== FUNÇÕES AUXILIARES ======== 

 

def registrar_operacao(extrato, tipo, valor): 

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 

    operacao = f"{timestamp} - {tipo}: R$ {valor:.2f}" 

    extrato.append(operacao) 

 

# ======== FUNÇÕES BANCÁRIAS ======== 

 

def depositar(saldo, valor, extrato, /): 

    if valor > 0: 

        saldo += valor 

        registrar_operacao(extrato, "Depósito", valor) 

        print("✅ Depósito realizado com sucesso.") 

    else: 

        print("❌ Valor inválido. Deposite apenas valores positivos.") 

    return saldo, extrato 

 

def sacar(*, saldo, valor, extrato, numero_saques): 

    if valor <= 0: 

        print("❌ Valor inválido. Saque apenas valores positivos.") 

    elif valor > saldo: 

        print("❌ Saldo insuficiente.") 

    elif valor > LIMITE_SAQUE: 

        print(f"❌ Saque excede o limite de R$ {LIMITE_SAQUE}.") 

    elif numero_saques >= LIMITE_SAQUES_DIARIOS: 

        print("❌ Limite diário de saques atingido.") 

    else: 

        saldo -= valor 

        numero_saques += 1 

        registrar_operacao(extrato, "Saque", valor) 

        print("✅ Saque realizado com sucesso.") 

    return saldo, extrato, numero_saques 

 

def mostrar_extrato(saldo, /, *, extrato): 

    print("\n================ EXTRATO ================\n") 

    if not extrato: 

        print("Não foram realizadas movimentações.") 

    else: 

        for linha in extrato: 

            print(linha) 

    print(f"\nSaldo atual: R$ {saldo:.2f}") 

    print("==========================================") 

 

# ======== FUNÇÕES DE USUÁRIO E CONTA ======== 

 

def criar_usuario(): 

    cpf = input("Informe o CPF (somente números): ").strip() 

    if any(usuario["cpf"] == cpf for usuario in usuarios): 

        print("❌ Já existe um usuário com esse CPF.") 

        return None 

 

    nome = input("Nome completo: ").strip() 

    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip() 

    endereco = input("Endereço (logradouro, número, bairro, cidade/UF): ").strip() 

 

    usuario = { 

        "nome": nome, 

        "data_nascimento": data_nascimento, 

        "cpf": cpf, 

        "endereco": endereco 

    } 

    usuarios.append(usuario) 

    print("✅ Usuário criado com sucesso!") 

    return usuario 

 

def encontrar_usuario_por_cpf(cpf): 

    for usuario in usuarios: 

        if usuario["cpf"] == cpf: 

            return usuario 

    return None 

 

def criar_conta(usuario): 

    numero_conta = len(contas) + 1 

    conta = { 

        "agencia": "0001", 

        "numero_conta": numero_conta, 

        "usuario": usuario 

    } 

    contas.append(conta) 

    print(f"✅ Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}") 

    return conta 

 

def encontrar_conta_por_usuario(usuario): 

    for conta in contas: 

        if conta["usuario"]["cpf"] == usuario["cpf"]: 

            return conta 

    return None 

 

def listar_contas(): 

    for conta in contas: 

        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}") 

 

# ======== OPERAÇÕES DO CLIENTE LOGADO ======== 

 

def menu_operacoes(usuario, conta): 

    saldo = 0 

    extrato = [] 

    numero_saques = 0 

 

    menu = f""" 

Bem-vindo(a), {usuario['nome']}! 

=============== MENU BANCÁRIO =============== 

 

[d] Depositar 

[s] Sacar 

[e] Extrato 

[q] Sair 

 

=> """ 

 

    while True: 

        opcao = input(menu).lower().strip() 

 

        if opcao == "d": 

            try: 

                valor = float(input("Informe o valor do depósito: ")) 

                saldo, extrato = depositar(saldo, valor, extrato) 

            except ValueError: 

                print("❌ Entrada inválida. Digite um número válido.") 

 

        elif opcao == "s": 

            try: 

                valor = float(input("Informe o valor do saque: ")) 

                saldo, extrato, numero_saques = sacar( 

                    saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques 

                ) 

            except ValueError: 

                print("❌ Entrada inválida. Digite um número válido.") 

 

        elif opcao == "e": 

            mostrar_extrato(saldo, extrato=extrato) 

 

        elif opcao == "q": 

            print("👋 Obrigado por utilizar nosso sistema. Até a próxima!") 

            break 

 

        else: 

            print("❌ Opção inválida. Por favor, escolha uma opção válida.") 

 

# ======== MENU INICIAL DO SISTEMA ======== 

 

def menu_inicial(): 

    while True: 

        print("\n====== BEM-VINDO AO BANCO PYTHON ======") 

        cpf = input("Já é nosso cliente? Insira seu CPF (ou pressione Enter para sair): ").strip() 

 

        if not cpf: 

            print("Saindo do sistema. Até logo!") 

            break 

 

        usuario = encontrar_usuario_por_cpf(cpf) 

 

        if usuario: 

            conta = encontrar_conta_por_usuario(usuario) 

            if conta: 

                menu_operacoes(usuario, conta) 

            else: 

                print("⚠️ Usuário encontrado, mas sem conta ativa.") 

                criar = input("Deseja criar uma conta agora? (s/n): ").lower() 

                if criar == "s": 

                    conta = criar_conta(usuario) 

                    menu_operacoes(usuario, conta) 

                else: 

                    print("Conta não criada. Retornando ao menu inicial.") 

        else: 

            print("❌ Usuário não encontrado.") 

            criar = input("Deseja se cadastrar como novo cliente? (s/n): ").lower() 

            if criar == "s": 

                novo_usuario = criar_usuario() 

                if novo_usuario: 

                    conta = criar_conta(novo_usuario) 

                    menu_operacoes(novo_usuario, conta) 

            else: 

                print("Cadastro não realizado. Retornando ao menu.") 

 

# ======== EXECUÇÃO ======== 

if __name__ == "__main__": 

    menu_inicial() 
