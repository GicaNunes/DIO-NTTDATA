# Função para realizar o depósito
def depositar(valor_deposito, saldo_conta):
    saldo_conta += valor_deposito
    return saldo_conta

# Função para realizar o saque
def sacar(valor_saque, saldo_conta, limite_saques, qnt_saques, limite_saque_diario):

    if qnt_saques >= limite_saque_diario:
        print('Caro cliente, desculpe, mas você excedeu o limite de três saques diários.')

    elif valor_saque > saldo_conta:
        print('Caro cliente, operação Inválida! Saldo Insuficiente!')

    elif valor_saque > limite_saques:
        print('Caro cliente, desculpe, mas o limite do saque é de até R$ 500,00.')
    else:
        saldo_conta -= valor_saque
        qnt_saques += 1
        return saldo_conta, qnt_saques, True
    return saldo_conta, qnt_saques, False

# Função para exibir o extrato da conta
def exibe_extrato(saldo_conta, extrato_conta):
    print('\n================ EXTRATO ================')

    if not extrato_conta:
        print('Não foram realizadas movimentações.')
    else:
        print(extrato_conta)
    print(f'\nSaldo: R$ {saldo_conta:.2f}')
    print('==========================================')

# Menu de opções do sistema
menu = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        Saudações! Seja Bem-Vindo ao Banco GIgiBank!
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Escolha uma das opções abaixo:
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q] Sair
Opção: """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao.lower() == 'd':
        print('\n================ DEPÓSITO ================\n')
        deposito = input('Caro cliente, informe o valor do depósito (ou digite "v" para retornar ao menu): ')
        if deposito.lower() == 'v':
            continue
        deposito = float(deposito)
        if deposito > 0:
            saldo = depositar(deposito, saldo)
            extrato += f'Depósito: R$ +{deposito:.2f}\n'
            print('Caro cliente, operação realizada com sucesso!')
        else:
            print('Não foi possível completar a operação. Informe um valor acima de zero.')
        input("Pressione Enter para continuar...")

    elif opcao.lower() == 's':
        print('\n================ SAQUE ================\n')
        valor = input('Caro cliente, informe o valor do saque (ou digite "v" para retornar ao menu): ')
        if valor.lower() == 'v':
            continue
        valor = float(valor)
        saldo, numero_saques, saque_realizado = sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES)
        if saque_realizado:
            extrato += f'Saque: R$ -{valor:.2f}\n'
            print('Caro cliente, operação realizada com sucesso!')
        input("Pressione Enter para continuar...")
    # Operação de extrato
    elif opcao.lower() == 'e':
        exibe_extrato(saldo, extrato)
        input("Pressione Enter para continuar...")

    elif opcao.lower() == 'q':
        break

    else:
        print('Opção inválida. Digite d - Depósito, s - Saque, e - Extrato, sa - Sair')