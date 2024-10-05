idade: int = int(input("Digite a sua idade: "))
carteira: float = float(input("Digite o valor da sua carteira: "))

# Tratar a idade
if idade < 18:
    print("Você é menor de idade! Não pode apostar!")
elif idade <= 25:
    print("Você é jovem! Pode apostar, mas tenha cuidado para não perder tudo!")
else:
    print("Você é adulto! Pode apostar com responsabilidade!")
    
# Tratar a carteira
if idade >= 18: 
    if carteira < 0:
        print("Você está devendo! Não pode apostar!")
    elif carteira < 100:
        print("Você tem pouco dinheiro! Pode apostar, mas tenha cuidado para não perder tudo!")
    elif carteira < 1000:
        print("Você tem dinheiro suficiente! Mas não é muito!")
    else:
        print("Você tem muito dinheiro! Pode apostar com responsabilidade!")