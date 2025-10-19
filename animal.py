class Animal:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        return "O animal emite um som"
        
    def apresentar(self, nome, idade):
        return f"Olá, eu sou {nome} e tenho {idade} anos"
        
class cachorro(Animal):
    def __init__ (self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
        
    def emitir_som(self):
        return "Au Au!"
        
class Gato(Animal):
    def __init__ (self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo
        
    def emitir_som(self):
         return "Miau!"
        
class Vaca(Animal):
    def __init__ (self, nome, idade, producao_leite_litros):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros
        
    def emitir_som(self):
        return "Muuuu!"
    
    #Método getter
    def obter_producao_leite(self):
        return self.__producao_leite_litros
    
    #Método setter
    def registrar_ordenha(self):
        self.__producao_leite_litros = self.__producao_leite_litros / 30