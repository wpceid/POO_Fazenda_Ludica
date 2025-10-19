class Animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        print("O animal emite um som")
        
    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos")