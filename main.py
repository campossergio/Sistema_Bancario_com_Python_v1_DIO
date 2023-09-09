menu = """

Selecione a opção desejada:

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Insira o valor desejado para realizar o seu Depósito!!! -> "))

        if valor_deposito > 0:
            saldo += valor_deposito
            print('Valor depositado: R$ {:.2f}, Saldo Atual: R$ {:.2f}'.format(valor_deposito, saldo))
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operação Inválida!!! O valor informado é negativo ou inválido.")

    elif opcao == "s":
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saque_excedido:
            print("Limite de Saques diários excedido!!!")
            print("O BANCO FOX K13 AGRADEÇE TENHA UM ÓTIMO DIA!!!")
            break

        print("Sacar")
        print("Valor máximo permitido para Saque R$500,00")
        valor_saque = float(input("Digite o valor desejado: "))
        if saldo < valor_saque or valor_saque > 500:
            print("Valor maior que Saldo disponível ou Valor maior que Limite Permitido, tente outro valor.")

        else:
            saldo -= valor_saque
            print(f"Valor sacado: R$ {valor_saque:.2f}, Saldo Atual: R$ {saldo:.2f}")
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("============  Extrato  ============")
        print("Não foram realizadas movimentções." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")

    elif opcao == "q":
        print("O BANCO FOX K13 AGRADEÇE TENHA UM ÓTIMO DIA!!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
