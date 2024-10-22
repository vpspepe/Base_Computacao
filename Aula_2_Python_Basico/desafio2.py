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
    
    # Calculo do Fator de Reducao
    if (tipo=="Básico"):
        fator_reducao: float = 0.0
    elif (tipo=="Prata"):
        fator_reducao: float = 0.05
    if (tipo=="Premium"):
        fator_reducao: float = 0.2

    while continuar_apostando:
        valor_apostado: float = float(input("Digite o valor apostado: "))
        valor_ganho: float = float(input("Digite o valor ganho: "))
        lucro_bruto: float = float(valor_ganho - valor_apostado)
        # Calculo do Imposto
        if lucro_bruto < 0:
            imposto: float = 0.0
        elif lucro_bruto < 100:
            imposto: float = 0.05 * lucro_bruto
        elif lucro_bruto < 1000:
            imposto: float = 0.15 * lucro_bruto
        elif lucro_bruto >= 1000: # Poderia ser escrito como "else:"
            imposto: float = 0.20 * lucro_bruto
        
        lucro_liquido: float = lucro_bruto - imposto * (1 - fator_reducao)
        
        # Atualização de Totais
        lucro_liquido_total += lucro_liquido
        valor_total_apostado += valor_apostado
        if lucro_bruto > 0:
            tips_bem_sucedidas += 1
        total_tips += 1
        imposto_total += imposto
        
        # Verificação de Saída
        parar_apostar: str = input("Voce deseja parar de apostar? Digite 'Sim' ou 'Nao': ")
        if parar_apostar == "Sim":
            continuar_apostando = False
            
    # Calculo da % de Tips Bem Suced
    tips_bem_sucedidas = (tips_bem_sucedidas / total_tips)
    print(f"Nome do Usuário: {nome}")
    print(f"Lucro liquido total: R$ {lucro_liquido_total}")
    print(f"Valor apostado total: R$ {valor_total_apostado}")
    print(f"% de tips bem sucedidas: {tips_bem_sucedidas}")
    print(f"Total imposto pago: R$ {imposto_total}")
        
        
    
