import numpy as np

temp_pacients = np.array([
    [39.6,38.4,36.5,36.4],
    [39.0,38.4,37.6,37.9],
    [37.5,37.1,36.3,36.0],
])
print(temp_pacients.dtype)

print(f'Temperatura pacient 1 el 1r dia.',temp_pacients[0][0])

print(f'Evolució temperatura pacient 3.',temp_pacients[2])

# Quins pacients tenen febre ?
print(temp_pacients>37.0)

# Provem què passa si tenim valors incorrectes.
temp_pacients = np.array([
    [39.6,38.4,36.5,36.4],
    [37.5,37.1,36.3,'x'],
])
print(temp_pacients)
# print(temp_pacients.sum()) # Dona error aquí

# I si tenim valors NaN ?
temp_pacients = np.array([
    [np.nan,38.4,36.5,36.4],
    [37.5,37.1,36.3,np.nan],
])
print(temp_pacients)
print(np.nanmax(temp_pacients))

# Provem mètode reshape i operació estadística.
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12]).reshape(2, 4)
print(grades[1:].min())
#print(grades.max())