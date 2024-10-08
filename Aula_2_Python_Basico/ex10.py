ganho_1: float = float(input("Quanto você ganhou? "))
ganho_2: float = float(input("Quanto você ganhou? "))

ganho : float = ganho_1 + ganho_2
imposto : float = 0.05*ganho
print(f"Você ganhou {ganho} reais.")
print(f"Você pagou {imposto} reais de imposto.")