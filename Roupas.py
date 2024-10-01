class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}"
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.telefone}"
class Venda:
    def __init__(self, cliente, produto):
        self.cliente = cliente
        self.produto = produto
    def __str__(self):
        return f"{self.cliente.nome} comprou {self.produto.nome}"
class Loja:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.vendas = []
    def cadastrar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        produto = Produto(nome, preco, quantidade)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso!")
    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        cliente = Cliente(nome, telefone)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self.produtos:
                print(produto)
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                print(cliente)
    def registrar_venda(self):
        self.listar_clientes()
        cliente_index = int(input("Escolha o índice do cliente: ")) - 1
        self.listar_produtos()
        produto_index = int(input("Escolha o índice do produto: ")) - 1
        if cliente_index < 0 or cliente_index >= len(self.clientes):
            print("Cliente inválido.")
            return
        if produto_index < 0 or produto_index >= len(self.produtos):
            print("Produto inválido.")
            return
        produto = self.produtos[produto_index]
        if produto.quantidade <= 0:
            print("Produto esgotado.")
            return
        produto.quantidade -= 1
        venda = Venda(self.clientes[cliente_index], produto)
        self.vendas.append(venda)
        print("Venda registrada com sucesso!")
    def listar_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada.")
        else:
            for venda in self.vendas:
                print(venda)
def main():
    loja = Loja()
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Produto")
        print("2. Cadastrar Cliente")
        print("3. Listar Produtos")
        print("4. Listar Clientes")
        print("5. Registrar Venda")
        print("6. Listar Vendas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            loja.cadastrar_produto()
        elif opcao == '2':
            loja.cadastrar_cliente()
        elif opcao == '3':
            loja.listar_produtos()
        elif opcao == '4':
            loja.listar_clientes()
        elif opcao == '5':
            loja.registrar_venda()
        elif opcao == '6':
            loja.listar_vendas()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    main()

