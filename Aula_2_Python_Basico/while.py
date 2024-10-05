def insere_valores_na_carteira():
    # Inicializa a variável 'carteira' com valor 0. Esta variável armazenará o valor total inserido.
    carteira: float = 0
    
    # Inicia um loop infinito que só será interrompido quando o usuário decidir parar.
    while True:
        # Solicita ao usuário que insira um valor e converte a entrada para float.
        valor: float = float(input("Digite o valor que deseja inserir na carteira: "))
        
        # Adiciona o valor inserido à variável 'carteira'.
        carteira += valor
        
        # Exibe o valor atual da carteira.
        print(f"O valor atual da sua carteira é {carteira}")
        
        # Pergunta ao usuário se ele deseja continuar inserindo valores.
        continuar: str = input("Deseja inserir mais algum valor na carteira? (S/N) ")
        
        # Se o usuário digitar 'N', o loop é interrompido.
        if continuar == "N":
            break
    
    # Retorna o valor total acumulado na carteira.
    return carteira

carteira: float = insere_valores_na_carteira()

print(f"O valor final da sua carteira é", carteira)

# Comentários explicativos:
# A função insere_valores_na_carteira inicializa a variável carteira com 0.
# Em seguida, entra em um loop infinito onde solicita ao usuário um valor para adicionar à carteira.
# O valor inserido é convertido para float e adicionado à carteira.
# O valor atual da carteira é exibido.
# O usuário é perguntado se deseja continuar inserindo valores.
# Se o usuário digitar "N", o loop é interrompido e a função retorna o valor final da carteira.
# Fora da função, o valor final da carteira é impresso.




