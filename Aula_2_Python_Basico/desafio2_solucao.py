# Cadastro de contas
nome1 = input("Digite o nome do usuário 1: ")
senha1 = input("Digite a senha do usuário 1: ")
login1 = input("Digite o login do usuário 1: ")
tipo1 = input("Digite o tipo do usuário 1 (Básico, Prata ou Premium): ")
saldo1 = float(input("Digite o saldo inicial do usuário 1: "))

nome2 = input("Digite o nome do usuário 2: ")
senha2 = input("Digite a senha do usuário 2: ")
login2 = input("Digite o login do usuário 2: ")
tipo2 = input("Digite o tipo do usuário 2 (Básico, Prata ou Premium): ")
saldo2 = float(input("Digite o saldo inicial do usuário 2: "))

nome3 = input("Digite o nome do usuário 3: ")
senha3 = input("Digite a senha do usuário 3: ")
login3 = input("Digite o login do usuário 3: ")
tipo3 = input("Digite o tipo do usuário 3 (Básico, Prata ou Premium): ")
saldo3 = float(input("Digite o saldo inicial do usuário 3: "))

# Verificação de login
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if (login == login1 and senha == senha1):
        nome = nome1
        tipo = tipo1
        break
    elif (login == login2 and senha == senha2):
        nome = nome2
        tipo = tipo2
        break
    elif (login == login3 and senha == senha3):
        nome = nome3
        tipo = tipo3
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")
        if input("Digite 'Sair' para encerrar ou pressione Enter para tentar novamente: ") == "Sair":
            exit()

# Solicitação de tips
total_apostado = 0
total_ganho = 0
total_tips = 0
tips_sucesso = 0
total_lucro_liquido = 0
total_imposto = 0

while True:
    valor_apostado = float(input("Digite o valor apostado: "))
    valor_ganho = float(input("Digite o valor ganho: "))

    total_apostado += valor_apostado
    total_ganho += valor_ganho
    total_tips += 1

    sucesso: bool = valor_ganho > valor_apostado
    if sucesso:
        tips_sucesso += 1

    # Cálculo do lucro para cada aposta
    lucro_bruto = valor_ganho - valor_apostado

    if lucro_bruto < 0:
        imposto_base = 0
    elif lucro_bruto <= 100:
        imposto_base = 0.05 * lucro_bruto
    elif lucro_bruto <= 1000:
        imposto_base = 0.15 * lucro_bruto
    else:
        imposto_base = 0.20 * lucro_bruto

    if tipo == "Básico":
        fator_reducao = 0
    elif tipo == "Prata":
        fator_reducao = 0.05
    elif tipo == "Premium":
        fator_reducao = 0.10

    imposto = imposto_base * (1 - fator_reducao)
    lucro_liquido = lucro_bruto - imposto

    total_lucro_liquido += lucro_liquido
    total_imposto += imposto

    print(f"Lucro Líquido da aposta: R$ {lucro_liquido:.2f}")
    print(f"Imposto Pago na aposta: R$ {imposto:.2f}")

    if input("Digite 'Sair' para encerrar ou pressione Enter para continuar: ") == "Sair":
        break

# Impressão dos resultados finais
print('\n', 100*'-', '\n')
print(f"Nome do usuário: {nome}")
print(f"Lucro Líquido Total: R$ {total_lucro_liquido:.2f}")
print(f"Valor Total Apostado: R$ {total_apostado:.2f}")
print(f"% de Tips bem sucedidas: {tips_sucesso / total_tips * 100:.2f}%")
print(f"Imposto Total Pago: R$ {total_imposto:.2f}")