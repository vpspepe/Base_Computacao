n_meses: int = int(input("Digite o número de meses: "))
mes_atual: int = 0
lucro_bruto_total: float = 0
apostado_total: float = 0

while (n_meses > mes_atual):
    lucro_bruto: float = float(input(f"Quanto voce ganhou no mes {mes_atual}? "))
    apostado_mes: float = float(input(f"Quanto você apostou no mês {mes_atual}?"))
    if lucro_bruto > 0:
        imposto_plataforma: float = 0.1 * lucro_bruto
        taxa_transasacao: float = 0.05 * lucro_bruto
        imposto: float = 0.02 * lucro_bruto
        lucro_liquido: float = lucro_bruto - imposto_plataforma - taxa_transasacao - imposto
        print(f"Voce pagou R$ {imposto_plataforma} para a platafoma!")
        print(f"Voce pagou R$ {taxa_transasacao} em taxas transacionais!")
        print(f"Voce pagou R$ {imposto} para o governo!")
        print(f"Seu lucro liquido foi de R$ {lucro_liquido}")
        print(f"Seu lucro bruto foi R$ {lucro_bruto}")
    else: 
        print("Você não teve lucro esse mês!")
        prejuizo: float = -1 * lucro_bruto
        print(f"Seu prejuizo foi de R$ {prejuizo}")
    lucro_bruto_total += lucro_bruto
    apostado_total += apostado_mes
    mes_atual += 1
    
print(f"Seu lucro bruto total foi de R$ {lucro_bruto_total}")
print(f"Você apostou um total de R$ {apostado_total}")
percentual:float = lucro_bruto_total / apostado_total
if lucro_bruto_total > 0:
    print(f"Seu lucro percentual total foi de", percentual)
else:
    print("Seu prejuízo percentual total foi de", -1*percentual)