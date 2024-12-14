# Sistema de Vendas com Cadastro de Usuários
def valida_usuario_e_senha(usuario: str, senha: str, usuarios: list):
    valid: bool = True
    # Validar usuario (deve ter mais de 5 caracteres)
    if len(usuario) > 5:
        for user in usuarios: # Não pode ser um usuário já existente
            if user['login'] == usuario:
                valid = False
    else:
        valid = False
    # Valida senha: deve ter mais de 5 caracteres
    if len(senha) <= 5:
        valid = False
    return valid

def conecta_com_banco_e_insere_usuario(nome: str, usuario: str, senha: str):
    ...

def insere_usuario(nome: str, usuario: str, senha: str, usuarios: list):
    conseguiu_inserir: bool = conecta_com_banco_e_insere_usuario(nome, usuario, senha)
    if conseguiu_inserir:
        print("Usuário cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar usuário!")
    usuarios.append({'nome': nome, 'login': usuario, 'senha': senha})
    print("Usuário cadastrado com sucesso!")
    return usuarios

def valida_e_insere_usuario(nome: str, usuario: str, senha: str, usuarios: list):
    valid = valida_usuario_e_senha(usuario, senha, usuarios)
    if valid:
        usuarios.append({'nome': nome, 'login': usuario, 'senha': senha})
        print("Usuário cadastrado com sucesso!")
    else:
        print("Usuário ou senha inválidos!")
    return usuarios

def cadastrar_usuarios():
    usuarios = []
    while True:
        nome = str(input("Digite o nome do usuário (ou 'Sair' para encerrar): "))
        if nome == 'Sair':
            break
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        usuarios.append({'nome': nome, 'login': login, 'senha': senha})
    return usuarios

def login(usuarios):
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    for usuario in usuarios:
        if usuario['login'] == login and usuario['senha'] == senha:
            return usuario
    return None

def menu_administrador(produtos):
    while True:
        opcao = input("Digite '1' para cadastrar produto ou 'Sair' para encerrar: ")
        if opcao == 'Sair':
            break
        elif opcao == '1':
            nome_produto = input("Digite o nome do produto: ")
            preco_produto = float(input("Digite o preço do produto: "))
            produtos.append({'nome': nome_produto, 'preco': preco_produto})
        else:
            print("Opção inválida!")

def menu_usuario(produtos):
    carrinho = []
    while True:
        print("Produtos disponíveis:")
        for i, produto in enumerate(produtos):
            print(f"{i+1}. {produto['nome']} - R${produto['preco']:.2f}")
        opcao = input("Digite o número do produto que deseja comprar (ou 'Sair' para encerrar): ")
        if opcao == 'Sair':
            break
        else:
            try:
                indice = int(opcao) - 1
                quantidade = int(input("Digite a quantidade: "))
                carrinho.append({'produto': produtos[indice], 'quantidade': quantidade})
            except (IndexError, ValueError):
                print("Opção inválida!")
    return carrinho

def calcular_total(carrinho):
    subtotal = sum(item['produto']['preco'] * item['quantidade'] for item in carrinho)
    if subtotal < 50:
        imposto = 0.05
    else:
        imposto = 0.025
    total = subtotal * (1 + imposto)
    return subtotal, imposto, total

def resumo_compra(carrinho, subtotal, imposto, total):
    print("\nResumo da Compra:")
    for item in carrinho:
        nome = item['produto']['nome']
        preco = item['produto']['preco']
        quantidade = item['quantidade']
        print(f"{nome} - {quantidade} x R${preco:.2f} = R${preco * quantidade:.2f}")
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Imposto: {imposto*100:.2f}%")
    print(f"Total: R${total:.2f}")

def main():
    usuarios = cadastrar_usuarios()
    produtos = []
    senha_administrador = "admin123"
    print(usuarios)
    
    while True:
        usuario = login(usuarios)
        if usuario:
            tipo_usuario = input("Você é administrador? (s/n): ")
            if tipo_usuario.lower() == 's':
                senha_extra = input("Digite a senha de administrador: ")
                if senha_extra == senha_administrador:
                    menu_administrador(produtos)
                else:
                    print("Senha de administrador incorreta!")
            else:
                carrinho = menu_usuario(produtos)
                if carrinho:
                    subtotal, imposto, total = calcular_total(carrinho)
                    resumo_compra(carrinho, subtotal, imposto, total)
        else:
            print("Login ou senha incorretos!")

if __name__ == '__main__':
    main()