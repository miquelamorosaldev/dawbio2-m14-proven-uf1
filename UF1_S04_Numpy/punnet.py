import numpy as np
import matplotlib.pyplot as plt

# Definición de alelos para el color del pelaje y el tipo de cola de los gatos
alelo_dominante_pelaje = 'P'
alelo_recesivo_pelaje = 'p'
alelo_dominante_cua = 'C'
alelo_recesivo_cua = 'c'

# Generación de los posibles genotipos para el pelaje y la cola de los gatos
genotips_pelatge = [alelo_dominante_pelaje + alelo_dominante_pelaje,
                    alelo_dominante_pelaje + alelo_recesivo_pelaje,
                    alelo_recesivo_pelaje + alelo_dominante_pelaje,
                    alelo_recesivo_pelaje + alelo_recesivo_pelaje]

genotips_cua = [alelo_dominante_cua + alelo_dominante_cua,
                 alelo_dominante_cua + alelo_recesivo_cua,
                 alelo_recesivo_cua + alelo_dominante_cua,
                 alelo_recesivo_cua + alelo_recesivo_cua]

# Creación del cuadro de Punnett
cuadro_punnett = np.array([[f"{pelaje}{cua}" for pelaje in genotips_pelatge] for cua in genotips_cua])

# Imprimir el cuadro de Punnett
print("Cuadro de Punnett para el ejercicio 5 (Gatos):")
print(cuadro_punnett)

# Cálculo de las probabilidades (assumint una segregació independent)
probabilitats = np.repeat(1/16,16).reshape(4,4).astype(float)


# Preguntas y respuestas adicionales
pregunta_5 = "¿Cuál es la probabilidad de que un gato tenga pelaje dominante (PpCC o PpCc)?"
respuesta_5 = "La probabilidad de que un gato tenga pelaje dominante es 0.5."

pregunta_6 = "Si los padres tienen genotipo PpCc y Ppcc, ¿cuál es la probabilidad de que un gato tenga pelaje recesivo y cola dominante (ppCC)?"
respuesta_6 = "La probabilidad de que un gato tenga pelaje recesivo y cola dominante es 0.0625."

pregunta_7 = "Supongamos que uno de los padres tiene genotipo PpCc y el otro ppCC. ¿Cuál es la probabilidad de que un gato tenga pelaje dominante y cola recesiva (Ppcc)?"
respuesta_7 = "La probabilidad de que un gato tenga pelaje dominante y cola recesiva es 0.0625."

pregunta_8 = "Si ambos padres tienen genotipo PpCc, ¿cuál es la probabilidad de que todos sus gatitos tengan pelaje dominante y cola dominante (PPCC)?"
respuesta_8 = "La probabilidad de que todos sus gatitos tengan pelaje dominante y cola dominante es 0.0625."

# Imprimir el cuadro dihíbrid y las probabilitats
print("\nProbabilitats:")
print(probabilitats)

# Imprimir preguntas y respuestas adicionales
print("\nPreguntas y Respuestas Adicionales:")
print(f"5. {pregunta_5} \n   {respuesta_5}")
print(f"6. {pregunta_6} \n   {respuesta_6}")
print(f"7. {pregunta_7} \n   {respuesta_7}")
print(f"8. {pregunta_8} \n   {respuesta_8}")

# Preguntas y respuestas adicionales
pregunta_5 = "¿Cuál es la probabilidad de que un gato tenga pelaje dominante (PpCC o PpCc)?"
respuesta_5 = "La probabilidad de que un gato tenga pelaje dominante es 0.5."

pregunta_6 = "Si los padres tienen genotipo PpCc y Ppcc, ¿cuál es la probabilidad de que un gato tenga pelaje recesivo y cola dominante (ppCC)?"
respuesta_6 = "La probabilidad de que un gato tenga pelaje recesivo y cola dominante es 0.0625."

pregunta_7 = "Supongamos que uno de los padres tiene genotipo PpCc y el otro ppCC. ¿Cuál es la probabilidad de que un gato tenga pelaje dominante y cola recesiva (Ppcc)?"
respuesta_7 = "La probabilidad de que un gato tenga pelaje dominante y cola recesiva es 0.0625."

pregunta_8 = "Si ambos padres tienen genotipo PpCc, ¿cuál es la probabilidad de que todos sus gatitos tengan pelaje dominante y cola dominante (PPCC)?"
respuesta_8 = "La probabilidad de que todos sus gatitos tengan pelaje dominante y cola dominante es 0.0625."

# Imprimir el cuadro dihíbrid y las probabilitats
print("\nProbabilitats:")
print(probabilitats)

# Imprimir preguntas y respuestas adicionales
print("\nPreguntas y Respuestas Adicionales:")
print(f"5. {pregunta_5} \n   {respuesta_5}")
print(f"6. {pregunta_6} \n   {respuesta_6}")
print(f"7. {pregunta_7} \n   {respuesta_7}")
print(f"8. {pregunta_8} \n   {respuesta_8}")


# Configuració dels colors per als alels
colors = {'PP': 'darkblue', 'Pp': 'mediumblue', 'pP': 'mediumblue', 'pp': 'lightblue',
          'CC': 'darkgreen', 'Cc': 'mediumseagreen', 'cC': 'mediumseagreen', 'cc': 'lightgreen'}


# Creació del gràfic del quadre de Punnett amb text
fig, ax = plt.subplots()
cax = ax.imshow(np.zeros_like(cuadro_punnett), cmap='Blues', vmin=0, vmax=1)

# Afegir text a les caselles
for i in range(len(genotips_cua)):
    for j in range(len(genotips_pelatge)):
        text = ax.text(j, i, cuadro_punnett[i, j], ha='center', va='center', color='black', fontsize=12)

# Afegir la llegenda dels colors
legend_labels = [plt.Line2D([0], [0], marker='o', color='w', label=label, markersize=10, markerfacecolor=color)
                 for label, color in colors.items()]
ax.legend(handles=legend_labels, loc='upper left', bbox_to_anchor=(1, 1))

# Afegir etiquetes
plt.xticks(range(len(genotips_pelatge)), genotips_pelatge)
plt.yticks(range(len(genotips_cua)), genotips_cua)

# Titol
plt.title('Quadre de Punnett - Gats (Pelatge i Cua)')

# Eliminar els eixos
ax.set_xticks([])
ax.set_yticks([])


#fig.add_legend('Age distribution by class')
plt.savefig('plot-dist1.png')


