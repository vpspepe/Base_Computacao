class Usuario:
    def __init__(self, nome, login, senha, is_admin=False):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.is_admin = is_admin

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class SistemaVendas:
    def __init__(self):
        self.usuarios = []
        self.produtos = []
        self.admin_senha_especial = "admin123"

    def cadastrar_usuario(self):
        while True:
            nome = input("Nome: ")
            login = input("Login: ")
            senha = input("Senha: ")
            is_admin = input("É administrador? (s/n): ").lower() == 's'
            if is_admin:
                senha_especial = input("Senha especial de administrador: ")
                if senha_especial != self.admin_senha_especial:
                    print("Senha especial incorreta. Usuário não cadastrado como administrador.")
                    is_admin = False
            self.usuarios.append(Usuario(nome, login, senha, is_admin))
            if input("Deseja cadastrar outro usuário? (s/n): ").lower() == 'n':
                break

    def login(self):
        login = input("Login: ")
        senha = input("Senha: ")
        for usuario in self.usuarios:
            if usuario.login == login and usuario.senha == senha:
                return usuario
        print("Login ou senha incorretos.")
        return None

    def cadastrar_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        self.produtos.append(Produto(nome, preco))

    def listar_produtos(self):
        for i, produto in enumerate(self.produtos):
            print(f"{i + 1}. {produto.nome} - R${produto.preco:.2f}")

    def comprar_produtos(self):
        carrinho = []
        while True:
            self.listar_produtos()
            escolha = int(input("Escolha o produto pelo número (0 para finalizar): "))
            if escolha == 0:
                break
            quantidade = int(input("Quantidade: "))
            produto = self.produtos[escolha - 1]
            carrinho.append((produto, quantidade))
        self.resumo_compra(carrinho)

    def resumo_compra(self, carrinho):
        subtotal = 0
        print("\nResumo da compra:")
        for produto, quantidade in carrinho:
            total_produto = produto.preco * quantidade
            subtotal += total_produto
            print(f"{produto.nome} - {quantidade} x R${produto.preco:.2f} = R${total_produto:.2f}")
        imposto = 0.05 if subtotal < 50 else 0.025
        total_imposto = subtotal * imposto
        total = subtotal + total_imposto
        print(f"Subtotal: R${subtotal:.2f}")
        print(f"Imposto: R${total_imposto:.2f}")
        print(f"Total: R${total:.2f}")

def main():
    sistema = SistemaVendas()
    sistema.cadastrar_usuario()
    usuario = sistema.login()
    if usuario:
        if usuario.is_admin:
            while True:
                print("\n1. Cadastrar produto\n2. Sair")
                escolha = int(input("Escolha: "))
                if escolha == 1:
                    sistema.cadastrar_produto()
                elif escolha == 2:
                    break
        else:
            sistema.comprar_produtos()

if __name__ == "__main__":
    main()