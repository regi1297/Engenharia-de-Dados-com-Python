
# Sistema Bancário em Python

Este é um sistema bancário simples implementado em Python. O sistema permite que os usuários realizem operações bancárias básicas como saques, depósitos, criação de contas e clientes, além de consultar o extrato de uma conta.

## Funcionalidades

- **Criar Cliente**: O usuário pode criar clientes informando nome, CPF, data de nascimento e endereço.
- **Criar Conta**: A partir de um cliente já criado, o usuário pode criar uma conta corrente associada a esse cliente.
- **Depositar**: Permite realizar depósitos em uma conta existente.
- **Sacar**: Permite realizar saques respeitando o saldo e o limite de saque por conta.
- **Exibir Extrato**: Mostra o extrato das transações realizadas em uma conta.
- **Listar Contas**: Exibe as informações de todas as contas criadas no sistema.

## Classes Principais

### Cliente
Classe base para representar um cliente do banco. Um cliente pode ter várias contas.

### PessoaFisica (herda de Cliente)
Representa um cliente pessoa física, com nome, CPF e data de nascimento.

### Conta
Classe base para representar uma conta bancária. Contém métodos para sacar, depositar e manter o histórico de transações.

### ContaCorrente (herda de Conta)
Conta bancária específica do tipo corrente, com limite de saque e número máximo de saques diários.

### Historico
Mantém o histórico das transações realizadas em uma conta.

### Transacao (Classe Abstrata)
Classe abstrata que define uma transação bancária. Classes concretas como `Saque` e `Deposito` herdam de `Transacao`.

### Saque (herda de Transacao)
Representa a operação de saque em uma conta bancária.

### Deposito (herda de Transacao)
Representa a operação de depósito em uma conta bancária.

## Uso do Sistema

### Menu de Opções

O sistema apresenta um menu onde o usuário pode escolher as seguintes operações:

```
=============== MENU ================
[d]    Depositar
[s]    Sacar
[e]    Extrato
[nc]   Nova conta
[lc]   Listar contas
[nu]   Novo cliente
[q]    Sair
```

### Como Usar

1. **Criar Cliente**: Escolha a opção "nu" e siga as instruções para criar um cliente.
2. **Criar Conta**: Após criar o cliente, escolha a opção "nc" para criar uma conta vinculada a esse cliente.
3. **Depositar**: Para depositar, escolha a opção "d", informe o CPF do cliente e o valor a ser depositado.
4. **Sacar**: Para sacar, escolha a opção "s", informe o CPF do cliente e o valor do saque.
5. **Exibir Extrato**: Para ver o extrato de uma conta, escolha "e" e informe o CPF do cliente.
6. **Listar Contas**: Para ver todas as contas criadas, escolha "lc".

### Exemplo de Uso

- Para criar um cliente e uma conta:
    ```
    Informe o CPF (somente número): 12345678900
    Informe o nome completo: João da Silva
    Informe a data de nascimento (dd-mm-aaaa): 10-05-1990
    Informe o endereço: Rua ABC, 123 - Bairro XYZ - Cidade/UF
    ```

- Para depositar:
    ```
    Informe o CPF do cliente: 12345678900
    Informe o valor do depósito: 100.50
    ```

- Para sacar:
    ```
    Informe o CPF do cliente: 12345678900
    Informe o valor do saque: 50.00
    ```

- Para ver o extrato:
    ```
    Informe o CPF do cliente: 12345678900
    ```

## Estrutura do Código

- O sistema utiliza **herança** e **polimorfismo** para modelar diferentes tipos de transações e clientes.
- As **classes abstratas** garantem que as transações tenham um método de registro consistente.
- A classe **Historico** mantém o registro de todas as transações associadas a uma conta.

## Requisitos

- Python 3.x

## Como Executar

Basta rodar o arquivo Python principal para iniciar o sistema:
```bash
python main.py
```

## Melhorias Futuras

- Implementar escolha de contas quando o cliente possuir mais de uma.
- Adicionar autenticação de cliente (ex: senha).
- Expandir para outros tipos de contas, como conta poupança.
