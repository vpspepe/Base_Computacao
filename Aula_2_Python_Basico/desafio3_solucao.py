
# Inicialização dos jogadores
nome1: str = "Jogador 1"
vitorias1: int = 0
total_partidas1: int = 0

nome2: str = "Jogador 2"
vitorias2: int = 0
total_partidas2: int = 0

nome3: str = "Jogador 3"
vitorias3: int = 0
total_partidas3: int = 0


while True:
    # Solicitação dos IDs dos jogadores
    id_jogador1: int = int(input("Digite o ID do primeiro jogador (1-3): "))
    id_jogador2: int = int(input("Digite o ID do segundo jogador (1-3, diferente do primeiro jogador): "))

    # Verificação do vencedor
    vencedor: int = int(input("Quem venceu? (1 para Jogador 1, 2 para Jogador 2): "))
    
    if vencedor == 1:
        if id_jogador1 == 1:
            vitorias1 += 1
        elif id_jogador1 == 2:
            vitorias2 += 1
        elif id_jogador1 == 3:
            vitorias3 += 1
    elif vencedor == 2:
        if id_jogador2 == 1:
            vitorias1 += 1
        elif id_jogador2 == 2:
            vitorias2 += 1
        elif id_jogador2 == 3:
            vitorias3 += 1

    if id_jogador1 == 1:
        total_partidas1 += 1
    elif id_jogador1 == 2:
        total_partidas2 += 1
    elif id_jogador1 == 3:
        total_partidas3 += 1

    if id_jogador2 == 1:
        total_partidas1 += 1
    elif id_jogador2 == 2:
        total_partidas2 += 1
    elif id_jogador2 == 3:
        total_partidas3 += 1

    # Pergunta se deseja continuar
    if input("Deseja cadastrar mais partidas? Digite 'Sair' para encerrar ou pressione Enter para continuar: ") == "Sair":
        break

# Impressão dos resultados finais
print('\n', 100*'-', '\n')

# Impressão dos resultados finais sem utilizar função
derrotas1 = total_partidas1 - vitorias1
percentual_vitorias1 = (vitorias1 / total_partidas1 * 100) if total_partidas1 > 0 else 0
print(f"Nome: {nome1}")
print(f"Total de Partidas Jogadas: {total_partidas1}")
print(f"Total de Vitórias: {vitorias1}")
print(f"Total de Derrotas: {derrotas1}")
print(f"Percentual de Vitórias: {percentual_vitorias1:.2f}%")
print('\n', 100*'-', '\n')

derrotas2 = total_partidas2 - vitorias2
percentual_vitorias2 = (vitorias2 / total_partidas2 * 100) if total_partidas2 > 0 else 0
print(f"Nome: {nome2}")
print(f"Total de Partidas Jogadas: {total_partidas2}")
print(f"Total de Vitórias: {vitorias2}")
print(f"Total de Derrotas: {derrotas2}")
print(f"Percentual de Vitórias: {percentual_vitorias2:.2f}%")
print('\n', 100*'-', '\n')

derrotas3 = total_partidas3 - vitorias3
percentual_vitorias3 = (vitorias3 / total_partidas3 * 100) if total_partidas3 > 0 else 0
print(f"Nome: {nome3}")
print(f"Total de Partidas Jogadas: {total_partidas3}")
print(f"Total de Vitórias: {vitorias3}")
print(f"Total de Derrotas: {derrotas3}")
print(f"Percentual de Vitórias: {percentual_vitorias3:.2f}%")
print('\n', 100*'-', '\n')