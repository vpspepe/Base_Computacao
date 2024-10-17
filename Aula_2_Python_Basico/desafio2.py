### ETAPA DE CADASTRO
nome_1: str = input("Digite o nome do usuário 1: ")
senha_1: str = input("Digite a senha do usuário 1: ")
login_1: str = input("Digite o login do usuário 1: ")
tipo_1: str = input("Digite o tipo do usuário 1: ")
saldo_inicial_1: float = float(input("Digite o saldo incial do usuário 1: "))

nome_2: str = input("Digite o nome do usuário 2: ")
senha_2: str = input("Digite a senha do usuário 2: ")
login_2: str = input("Digite o login do usuário 2: ")
tipo_2: str = input("Digite o tipo do usuário 2: ")
saldo_inicial_2: float = float(input("Digite o saldo incial do usuario 2: "))

nome_3: str = input("Digite o nome do usuário 3: ")
senha_3: str = input("Digite a senha do usuário 3: ")
login_3: str = input("Digite o login do usuário 3: ")
tipo_3: str = input("Digite o tipo do usuário 3: ")
saldo_inicial_3: float = float(input("Digite o saldo incial do usuario 3: "))

### ETAPA DE LOGIN
sair: bool = False
login_aceito: bool = False
while (sair == False) and (login_aceito == False):
    login: str = input("Digite seu login: ")
    senha: str = input("Digite sua senha: ")
    
    if (login == login_1) and (senha == senha_1):
        nome: str = nome_1
        tipo: str = tipo_1
        saldo_inicial: float = saldo_inicial_1
        login_aceito = True
    
    elif (login == login_2) and (senha == senha_2):
        nome: str = nome_2
        tipo: str = tipo_2
        saldo_inicial: float = saldo_inicial_2
        login_aceito = True
        
    elif (login == login_3) and (senha == senha_3):
        nome: str = nome_3
        tipo: str = tipo_3
        saldo_inicial: float = saldo_inicial_3
        login_aceito = True
        
    else:
        print("Erro no login")
        tentar_novamente: str = input("Para continuar aperte \"Enter\" e para sair digite \"Sair\" ")
        sair = (tentar_novamente == "Sair")

### ETAPA DE APOSTAS
if login_aceito == True:
    continuar_apostando: bool = True
    lucro_liquido_total: float = 0
    valor_total_apostado: float = 0
    tips_bem_sucedidas: int = 0
    total_tips: int = 0
    imposto_total: float = 0

    
    while continuar_apostando:
        valor_apostado: float = float(input("Digite o valor apostado: "))
        valor_ganho: float = float(input("Digite o valor ganho: "))
    
