
class Tip:
    def __init__(self, time, campeonato, data, odd, resultado):
        self.time = time
        self.campeonato = campeonato
        self.data = data
        self.odd = odd
        self.resultado = resultado
        
class Tipster:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.tips = []
    
    def cadastrar_tip(self, tip: Tip):
        self.tips.append(tip)
        print("Nova tip adicionada ao usuário", self.nome, "do time do", tip.time)
        
    def listar_tips(self):
        for tip in self.tips:
            print(f"{tip.time} - {tip.campeonato} - {tip.data} - {tip.odd} - {tip.resultado}")
    



if __name__ == "__main__":
    tip1 = Tip("Flamengo", "Brasileirão", "2021-09-01", 1.5, "V")
    tip2 = Tip("Bahia", "Brasileirão", "2021-09-01", 1.5, "V")
    tip3 = Tip("Cruzeiro", "Brasileirão", "2021-09-01", 1.5, "V")
    tipster1 = Tipster("João", 30, "joao@gmail.com", "123456789")
    tipster1.cadastrar_tip(tip1)
    tipster1.cadastrar_tip(tip2)
    tipster1.cadastrar_tip(tip3)
    tipster1.listar_tips()
        
    
    