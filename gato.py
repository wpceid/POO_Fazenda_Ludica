from animal import Animal

class Gato(Animal):
    def __init__ (self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo
        
    def emitir_som(self):
        print("Miau!")