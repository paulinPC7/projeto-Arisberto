class Produto {
    constructor(nome, preco, quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }
    toString() {
        return `Produto: ${this.nome}, Preço: R$${this.preco.toFixed(2)}, Quantidade: ${this.quantidade}`;
    }
}
class Cliente {
    constructor(nome, email) {
        this.nome = nome;
        this.email = email;
    }
    toString() {
        return `Cliente: ${this.nome}, Email: ${this.email}`;
    }
}
class Loja {
    constructor() {
        this.produtos = [];
        this.clientes = [];
    }
    cadastrarProduto(nome, preco, quantidade) {
        const produto = new Produto(nome, preco, quantidade);
        this.produtos.push(produto);
        console.log("Produto cadastrado com sucesso!");
    }
    cadastrarCliente(nome, email) {
        const cliente = new Cliente(nome, email);
        this.clientes.push(cliente);
        console.log("Cliente cadastrado com sucesso!");
    }
    listarProdutos() {
        if (this.produtos.length === 0) {
            console.log("Nenhum produto cadastrado.");
        } else {
            this.produtos.forEach(produto => console.log(produto.toString()));
        }
    }

    listarClientes() {
        if (this.clientes.length === 0) {
            console.log("Nenhum cliente cadastrado.");
        } else {
            this.clientes.forEach(cliente => console.log(cliente.toString()));
        }
    }
}
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout});
const loja = new Loja();
function menu() {
    console.log("\n--- Menu ---");
    console.log("1. Cadastrar Produto");
    console.log("2. Cadastrar Cliente");
    console.log("3. Listar Produtos");
    console.log("4. Listar Clientes");
    console.log("5. Sair");
    readline.question("Escolha uma opção: ", opcao => {
        switch (opcao) {
            case '1':
                readline.question("Digite o nome do produto: ", nome => {
                    readline.question("Digite o preço do produto: ", preco => {
                        readline.question("Digite a quantidade do produto: ", quantidade => {
                            loja.cadastrarProduto(nome, parseFloat(preco), parseInt(quantidade));
                            menu();});});});
                break;
            case '2':
                readline.question("Digite o nome do cliente: ", nome => {
                    readline.question("Digite o email do cliente: ", email => {
                        loja.cadastrarCliente(nome, email);
                        menu();});});
                break;
            case '3':
                loja.listarProdutos();
                menu();
                break;
            case '4':
                loja.listarClientes();
                menu();
                break;
            case '5':
                console.log("Saindo...");
                readline.close();
                break;
            default:
                console.log("Opção inválida, tente novamente.");
                menu();}});
}
menu();

