num_semanas: int = int(input("Digite o número de semanas: "))
total: float = 0.0
semana_atual: int = 0

while (semana_atual < num_semanas):
    ganho_semana: float = float(input(f"Digite quanto voce ganhou na semana {semana_atual}: "))
    total = total + ganho_semana
    semana_atual = semana_atual + 1
    
media: float = total / num_semanas

print(f"Voce ganhou {total} reais.")
print(f"A sua média foi {media} reais por semana.")
print(f"Isso aconteceu ao longo de {num_semanas} semanas.")