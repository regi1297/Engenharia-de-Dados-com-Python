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
    - É criado e atualizado automaticamente quando o sistema é executado.

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
O sistema exibe este menu e aguarda a escolha do usuário, que deve digitar a letra correspondente à ação desejada.

Depositar
Para realizar um depósito, o sistema solicita um valor ao usuário. Esse valor é validado para garantir que seja positivo. 
Caso seja válido, o saldo é atualizado e a transação é registrada no extrato. O sistema salva as mudanças no arquivo logo 
após o depósito.


if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\\n"
        salvar_dados(saldo, numero_saques, extrato)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
