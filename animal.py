class animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def EmitirSom(self):
        print("O animal emite um som")
        
    def Apresentar(self, nome, idade):
        print(f"Olá, eu sou {nome} e tenho {idade} anos")
        
class cachorro(animal):
    def __init__ (self, nome, idade, raca):
        animal.nome = nome
        animal.idade = idade
        self.raca = raca
        
    def EmitirSom(animal):
        print("Au Au!")