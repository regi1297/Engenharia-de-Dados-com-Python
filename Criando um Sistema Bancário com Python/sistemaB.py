import os

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Carregar o saldo e extrato de um arquivo, se ele existir
if os.path.exists("dados_banco.txt"):
    with open("dados_banco.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        saldo = float(linhas[0].strip())  # Carregar o saldo
        numero_saques = int(linhas[1].strip())  # Carregar o número de saques
        extrato = "".join(linhas[2:])  # Carregar o extrato
else:
    saldo = 0
    extrato = ""
    numero_saques = 0

limite = 500  # Limite de saque por transação
LIMITE_SAQUES = 3  # Limite de saques diários

# Função para salvar os dados no arquivo
def salvar_dados(saldo, numero_saques, extrato):
    with open("dados_banco.txt", "w") as arquivo:
        arquivo.write(f"{saldo}\n")
        arquivo.write(f"{numero_saques}\n")
        arquivo.write(extrato)

# Loop principal do sistema bancário
while True:
    opcao = input(menu)  # Exibe o menu e captura a escolha do usuário

    # Depósito
    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor  # Atualiza o saldo com o valor do depósito
                extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra o depósito no extrato
                salvar_dados(saldo, numero_saques, extrato)  # Salva os dados no arquivo
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Erro! O valor deve ser numérico.")

    # Saque
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))

            # Verificações de regras de negócio
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            # Mensagens de erro específicas
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
            elif excedeu_saques:
                print(f"Operação falhou! Você atingiu o número máximo de {LIMITE_SAQUES} saques diários.")
            elif valor > 0:
                saldo -= valor  # Atualiza o saldo subtraindo o valor do saque
                extrato += f"Saque: R$ {valor:.2f}\n"  # Registra o saque no extrato
                numero_saques += 1  # Incrementa o contador de saques
                salvar_dados(saldo, numero_saques, extrato)  # Salva os dados no arquivo
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Erro! O valor deve ser numérico.")

    # Extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        # Verifica se houve transações
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)  # Exibe o histórico de transações
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    # Sair
    elif opcao == "q":
        print("Encerrando o sistema bancário. Obrigado por utilizar nossos serviços!")
        salvar_dados(saldo, numero_saques, extrato)  # Salva os dados antes de sair
        break  # Encerra o loop principal e o programa

    # Opção inválida
    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")
