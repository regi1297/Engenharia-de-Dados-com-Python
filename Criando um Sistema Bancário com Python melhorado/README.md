# Sistema de Gerenciamento Bancário

Este projeto é um sistema simples de gerenciamento bancário desenvolvido em Python. O sistema permite a realização de depósitos, saques, visualização de extratos, e a gestão de usuários e contas bancárias.

## Funcionalidades

- **Depositar:** Adiciona um valor ao saldo da conta.
- **Sacar:** Retira um valor do saldo da conta, respeitando limites e condições.
- **Extrato:** Exibe o saldo atual e o histórico de transações.
- **Nova Conta:** Cria uma nova conta bancária para um usuário existente.
- **Listar Contas:** Lista todas as contas cadastradas.
- **Novo Usuário:** Adiciona um novo usuário ao sistema.

## Estrutura do Código

### Funções

1. **menu()**
   - Exibe o menu principal e retorna a opção selecionada pelo usuário.

2. **depositar(saldo, valor, extrato)**
   - Realiza um depósito na conta se o valor for positivo.
   - Atualiza o saldo e o extrato com a transação.

3. **sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)**
   - Realiza um saque na conta se o valor for válido e dentro dos limites estabelecidos.
   - Atualiza o saldo, o extrato e o número de saques realizados.

4. **exibir_extrato(saldo, extrato)**
   - Exibe o extrato da conta e o saldo atual.

5. **criar_usuario(usuarios)**
   - Cria um novo usuário se o CPF não estiver cadastrado.
   - Solicita informações como nome, data de nascimento e endereço.

6. **filtrar_usuario(cpf, usuarios)**
   - Filtra e retorna o usuário com o CPF fornecido.

7. **criar_conta(agencia, numero_conta, usuarios)**
   - Cria uma nova conta para um usuário existente com base no CPF fornecido.

8. **listar_contas(contas)**
   - Lista todas as contas cadastradas no sistema.

9. **main()**
   - Função principal que gerencia o menu e as operações da conta.
   - Controla o fluxo das operações do sistema bancário.

## Como Usar

1. Execute o arquivo Python para iniciar o sistema:
   ```bash
   python sistemaB.py
