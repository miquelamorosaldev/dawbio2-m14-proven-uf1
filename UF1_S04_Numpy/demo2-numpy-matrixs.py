
# Problema de matrius 
# Una firma de automóviles dispone de dos plantas de fabricación una en España y otra en Inglaterra, en
# los que fabrica dos modelos de coches M1 y M2, de tres colores x, y, z. Su capacidad de producción
# diaria en cada planta está dada por las siguientes matrices (A para España y B para Inglaterra).
# http://sauce.pntic.mec.es/~agarci28/SEGUNDO/Matrices_y_Determinantes/Problemas%20de%20interpretacion%20de%20matrices.pdf
import numpy as np

ar_vendes_es = np.array([
    [ 300, 95],
    [ 250, 100],
    [ 200, 100]
])

ar_vendes_uk = np.array([
    [ 190, 90],
    [ 200, 100],
    [ 150, 80]
])

def prob_a(arr_vesp: np.array, arr_vuk: np.array) -> np.array:
    '''Determinar la representación matricial de la producción total por día.
        Input: arr_vesp -> Array ventas en España por día
        arr_vuk -> Array ventas en UK por día
        Output: Array ventas de los 2 paises por día
    '''
    return ar_vendes_es + ar_vendes_uk

def prob_b(arr_vesp: np.array, arr_vuk: np.array) -> np.array:
    '''Si se eleva la producción en España un 20% y se disminuye en Inglaterra un 10% \
      ¿qué matriz representa la nueva producción total?
        Input: arr_vesp -> Array ventas en España por día
        arr_vuk -> Array ventas en UK por día
        Output: Array ventas finales 2 paises por día.
    '''
    ar_vendes_es_2 = arr_vesp*1.2
    ar_vendes_uk_2 = arr_vuk*0.9
    return ar_vendes_es_2 + ar_vendes_uk_2


print('a) Determinar la representación matricial de la producción total por día.')
ar_vendes_total_1 = ar_vendes_es + ar_vendes_uk
print(ar_vendes_total_1)

# Expected result p1.
# [[490 185]
#  [450 200]
#  [350 180]]

print('b) Si se eleva la producción en España un 20% y se disminuye en Inglaterra un 10% \
      ¿qué matriz representa la nueva producción total?')
ar_vendes_es_2 = ar_vendes_es*1.2
ar_vendes_uk_2 = ar_vendes_uk*0.9
ar_vendes_total_2 = ar_vendes_es_2 + ar_vendes_uk_2
print(ar_vendes_total_2)

# Expected result p2.
# [[531. 195.]
#  [480. 210.]
#  [375. 192.]]
