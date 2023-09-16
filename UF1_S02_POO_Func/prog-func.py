# Exemple funció map.
def mult3 (num: float) -> float:
    return num * 3

# range genera sequències de números
# range (num_ini, num_fin, step)
llistaNums: float = list(range(10,40,2))
print("Llista números original.")
print(llistaNums)
print("Llista números multiplicats per 3.")
llistaNumsPer3 = list(map(mult3,llistaNums))
print(llistaNumsPer3)

# Exemple funció filter.
def greaterOrEqual5 (num: float) -> bool:
    return num >= 5

llistaNotes: float = [8,5,6.2,4.2,10,6.8,3.4,7.9,9.3,8,2.4,9.7,7.6]

print("Llista notes original.")
print(llistaNotes)

print("Llista notes majors o iguals a 5.")
llistaNotesMajorsIguals5 = list(filter(greaterOrEqual5,llistaNotes))

print(llistaNotesMajorsIguals5)

print("Percentatge aprovats.")
# Dividim la longitud de les notes >5 respecte el total de notes 
# La funció len ens permet veure el número d'elements de les llistes. 
percAprov: int = len(llistaNotesMajorsIguals5) / len(llistaNotes)

## Per arrodonir a 2 decimals usem funció round.
print( str( round(percAprov,4)*100) + ' %')

# Exemple funció zip.
paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
print(list(zip(paises, poblaciones)))

# [('China', 1391), ('India', 1364), ('Estados Unidos', 327), ('Indonesia', 264)]
for pais, poblacion in zip(paises, poblaciones):
    print("{}: {} millones de habitantes.".format(pais, poblacion))

# Exemple funció reduce.

from functools import reduce
producto = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(producto)
# Salida: 24
