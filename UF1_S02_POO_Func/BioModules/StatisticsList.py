class StatisticsList():  # els 'docstring' s'escriuran sota la declaració amb triples cometes
    """ aquesta classe contindrà mètodes per a fer estadístiques sobre una llista de numeros"""
 
    def __init__(self, numeros):
        # és habitual usar per a l'atribut el mateix identificador del paràmetre
        # print(numeros)
        self.numeros = numeros  # atribut d'instància que pren el valor del paràmetre

    def __str__ (self):
        # Retorna un string amb les dades més importants de la classe
        return 'Contingut de la llista' + str(self.numeros)
    
    def sumatori(self):
        """ Retorna la suma de tots els números  """
        return sum(self.numeros)
