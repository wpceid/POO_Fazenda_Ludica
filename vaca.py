from animal import Animal

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