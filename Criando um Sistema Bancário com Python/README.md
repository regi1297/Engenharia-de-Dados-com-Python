
# Sistema Bancário em Python

## Sumário

1. [Descrição Geral](#descrição-geral)
2. [Requisitos](#requisitos)
3. [Funcionalidades](#funcionalidades)
4. [Estrutura do Sistema](#estrutura-do-sistema)
5. [Explicação do Código](#explicação-do-código)
    - [Menu](#menu)
    - [Depositar](#depositar)
    - [Sacar](#sacar)
    - [Extrato](#extrato)
    - [Sair](#sair)
    - [Função de Salvamento](#função-de-salvamento)
6. [Validações de Entrada](#validações-de-entrada)
7. [Persistência de Dados](#persistência-de-dados)
8. [Exemplo de Execução](#exemplo-de-execução)

---

## Descrição Geral

Este sistema bancário em Python simula um conjunto básico de operações bancárias, permitindo ao usuário realizar depósitos, saques, visualizar o extrato de suas movimentações e encerrar a sessão. O sistema implementa regras de negócio como limite diário de saques e limite por valor de saque.

Além disso, o sistema salva os dados do saldo, número de saques e extrato em um arquivo de texto, permitindo que as informações sejam recuperadas entre diferentes execuções.

## Requisitos

- Python 3.6 ou superior
- Sistema de arquivos com permissão para leitura e escrita

## Funcionalidades

1. **Depositar**: O usuário pode adicionar dinheiro à conta. O valor deve ser maior que zero.
2. **Sacar**: O usuário pode retirar dinheiro, desde que tenha saldo suficiente, não ultrapasse o limite de saque por transação e respeite o número máximo de saques diários.
3. **Extrato**: O usuário pode consultar o histórico de transações (depósitos e saques) e visualizar o saldo atual.
4. **Sair**: O sistema encerra a sessão e salva os dados de saldo, extrato e número de saques em um arquivo.
5. **Persistência de dados**: As informações são gravadas em um arquivo chamado `dados_banco.txt`, garantindo que o saldo, número de saques e extrato permaneçam entre execuções.

---

## Estrutura do Sistema

- **Arquivo `dados_banco.txt`**:
    - Armazena o saldo, número de saques e extrato de transações.
    - Sendo criado e atualizado automaticamente quando o sistema é executado.

## Explicação do Código

### Menu

O menu apresenta ao usuário as opções disponíveis:

```python
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
```

O sistema exibe este menu e aguarda a escolha do usuário, que deve digitar a letra correspondente à ação desejada.

### Depositar

Para realizar um depósito, o sistema solicita um valor ao usuário. Esse valor é validado para garantir que seja positivo. Caso seja válido, o saldo é atualizado e a transação é registrada no extrato. O sistema salva as mudanças no arquivo logo após o depósito.

```python
if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        salvar_dados(saldo, numero_saques, extrato)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
```

### Sacar

No caso do saque, o sistema impõe várias restrições:
- O valor não pode ser maior que o saldo disponível.
- O valor não pode exceder o limite definido por transação (R$ 500,00).
- O número de saques diários não pode exceder o limite de 3.

Se todas as condições forem atendidas, o saldo é atualizado, o saque é registrado no extrato, o número de saques é incrementado, e os dados são salvos no arquivo.

```python
elif opcao == "s":
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print(f"Operação falhou! Você atingiu o número máximo de {LIMITE_SAQUES} saques diários.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        salvar_dados(saldo, numero_saques, extrato)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
```

### Extrato

O extrato exibe todas as transações (depósitos e saques) realizadas até o momento, juntamente com o saldo atual. Se não houver transações, o sistema exibe uma mensagem indicando que não foram realizadas movimentações.

```python
elif opcao == "e":
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")
```

### Sair

Quando o usuário escolhe a opção "Sair", o sistema salva os dados de saldo, extrato e número de saques no arquivo `dados_banco.txt`, garantindo que essas informações estarão disponíveis na próxima execução.

```python
elif opcao == "q":
    print("Encerrando o sistema bancário. Obrigado por utilizar nossos serviços!")
    salvar_dados(saldo, numero_saques, extrato)
    break
```

### Função de Salvamento

A função `salvar_dados()` é responsável por gravar os dados no arquivo `dados_banco.txt`. Ela é chamada sempre que uma operação que modifica o saldo ou o extrato é realizada.

```python
def salvar_dados(saldo, numero_saques, extrato):
    with open("dados_banco.txt", "w") as arquivo:
        arquivo.write(f"{saldo}\n")
        arquivo.write(f"{numero_saques}\n")
        arquivo.write(extrato)
```

## Validações de Entrada

Para garantir que o sistema funcione corretamente, há verificações para:
- Valores de depósito e saque numéricos.
- Verificação de saldo insuficiente.
- Limite de valor de saque por transação (R$ 500,00).
- Limite de saques diários (máximo de 3).

Se o usuário inserir um valor inválido, uma mensagem de erro é exibida.

## Persistência de Dados

Os dados de saldo, número de saques e extrato são gravados no arquivo `dados_banco.txt` a cada operação. O sistema carrega esses dados do arquivo quando é executado, permitindo que o usuário continue de onde parou em execuções anteriores.

---

## Exemplo de Execução

1. **Depósito**:
    ```
    Informe o valor do depósito: 100.00
    Depósito de R$ 100.00 realizado com sucesso.
    ```

2. **Saque**:
    ```
    Informe o valor do saque: 50.00
    Saque de R$ 50.00 realizado com sucesso.
    ```

3. **Extrato**:
    ```
    ================== EXTRATO ==================
    Depósito: R$ 100.00
    Saque: R$ 50.00

    Saldo atual: R$ 50.00
    =============================================
    ```

4. **Sair**:
    ```
    Encerrando o sistema bancário. Obrigado por utilizar nossos serviços!
    ```

---
