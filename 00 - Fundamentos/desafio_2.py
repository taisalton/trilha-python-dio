import textwrap

def saque(*, saldo, valor, extrato, limite, numero_saques,lim_saques):
    limite_valor = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= lim_saques
    if limite_valor:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def deposito(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return (saldo, extrato)

def cad_usuario(usuarios):
    cpf = int(input('Digite os números do cpf'))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um usuário com esse CPF')
        return
    
    nome = input('Digite o nome do seu usuário')
    data_nascimento = input('Digite a data de nascimento')
    endereço = input('Digite o seu endereço')
    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereço})
    print('Usuário criado com sucesso')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cad_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('Usuário não encontrado! Tente novamente!')

def menu():
    menu = """\n
    **************** MENU ****************
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tCriar novo usuário
    [nc]\tCriar nova conta
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    agencia = '0001'
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = int(input("Digite o valor do depósito"))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor do saque"))
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                lim_saques = LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == "nu":
            cad_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = cad_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
