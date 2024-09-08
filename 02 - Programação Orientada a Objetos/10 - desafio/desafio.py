##Descrição: Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

##Tarefas:

##Método adicionar_venda: Na classe Categoria, crie um método chamado adicionar_venda que adiciona um objeto Venda à lista de vendas da categoria.

##Método total_vendas: Na classe Categoria, crie um método chamado total_vendas que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

##Na função main:

##Entrada de Dados:

##Leia o nome das categorias e, para cada categoria, leia as vendas associadas.

##Implementação: Adicione cada venda à categoria correspondente usando o método adicionar_venda.

##Exibição dos Resultados:

##Exiba o total de vendas para cada categoria.

##Implementação: Utilize o método total_vendas para calcular e exibir o total das vendas.

##Entrada
##A entrada consiste em:

##Nome da Categoria (string)

##Lista de Vendas (com as colunas Produto, Quantidade, Valor)
##Saída
##A saída é o total de vendas por categoria.

# entrada:
#Eletrônicos:
#Celular, 5, 1000
#Fone de Ouvido, 10, 500
#Móveis:
#Mesa, 2, 800 = 400
#Cadeira, 4, 400
#Alimentos:
#Arroz, 10, 200
#Feijão, 7, 140
#Jardinagem:
#Planta, 2, 60
#Ferramentas, 1, 100
#Livros:
#Aventuras no Tempo, 1, 80
#Mistérios do Oceano, 2, 90
#Esportes:
#Tênis, 7, 210
#Bola, 3, 120

#Saídas esperadas:
#Vendas em Eletrônicos: 1500.0
#Vendas em Móveis: 1200.0

#Vendas em Alimentos: 340.0
#Vendas em Jardinagem: 160.0

#Vendas em Livros: 170.0
#Vendas em Esportes: 330.0

# montar o sistema para inserir as entradas e obter as saidas:

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

    def total(self):
        return self.quantidade * self.valor


class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_vendas(self):
        return sum(venda.total() for venda in self.vendas)


def main():
    categorias = {}

    while True:
        nome_categoria = input("Digite o nome da categoria (ou 'sair' para finalizar): ")
        if nome_categoria.lower() == 's':
            break

        if nome_categoria not in categorias:
            categorias[nome_categoria] = Categoria(nome_categoria)

        while True:
            produto = input(f"Digite o nome do produto da categoria {nome_categoria} (ou 'sair' para mudar de categoria): ")
            if produto.lower() == 's':
                break
            quantidade = int(input(f"Digite a quantidade de {produto}: "))
            valor = float(input(f"Digite o valor de {produto}: "))

            venda = Venda(produto, quantidade, valor)
            categorias[nome_categoria].adicionar_venda(venda)

    print("\nRelatório de Vendas por Categoria:")
    for categoria in categorias.values():
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas():.2f}")


if __name__ == "__main__":
    main()
