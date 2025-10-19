class Animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        print("O animal emite um som")
        
    def apresentar(self, nome, idade):
        print(f"Olá, eu sou {nome} e tenho {idade} anos")
        
class cachorro(Animal):
    def __init__ (self, nome, idade, raca):
        Animal.nome = nome
        Animal.idade = idade
        self.raca = raca
        
    def emitir_som(Animal):
        print("Au Au!")
        
class gato(Animal):
    def __init__ (self, nome, idade, cor_pelo):
        Animal.nome = nome
        Animal.idade = idade
        self.cor_pelo = cor_pelo
        
    def emitir_som(Animal):
        print("Miau!")
        
class vaca(Animal):
    def __init__ (self, nome, idade, producao_leite_litros):
        Animal.nome = nome
        Animal.idade = idade
        self.producao_leite_litros = producao_leite_litros
        
    def emitir_som(Animal):
        print("Muuuu!")