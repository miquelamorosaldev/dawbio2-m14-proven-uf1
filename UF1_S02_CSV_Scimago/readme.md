# Sessió 2.2 Consultes sobre un fitxer CSV a la base de dades Scimago.

## [Document sobre com descarregar fitxer CSV i llegir-lo amb Python.](https://docs.google.com/document/d/16WI0NI6WESHgJkEk3WOCURFxgjJ6OqLbCN7HNcuCQoo/edit)

## Codi de l'enunciat.

L'objectiu d'aquest exercici és realitzar diverses consultes amb Python, i repassar els fonaments: funcions, llistes, sets, diccionaris, prog.funcional...

Recomanem organitzar el codi de l'exercici tal i com està en aquesta carpeta; posar cada consulta  en una funció (la q1 ja està resolta) i tenir per separat la classe que llegeix i tracta els fitxers CSV.

## Consultes Sessió 2

Q1 - How many entries are in scimago-medicine.csv?

Q2 - Show the first 25 entries.

Q3 - How many entries are from Spain? (Country = Spain)

Hint Q3:
```python
for entry in entries:
	entry['Country'] == 'Spain'
```

Q4 - Show all the journals (Type = journal) published in UK (Country = United Kingdom) with an 

H-Index greater than 200, sorted by H-index (biggest H-Index first)

Hint:
https://stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python

Q5 - What types of scientific publications are in the file (paràmetre Type)?

Hint; expected result:
```python
['journal', 'book series', 'conference and proceedings', 'trade journal']
```

Q6 - Count the number of types of each scientific publication.

Q7 - Show all regions covered by all entries.

Hint; expected result:
```python
{'Northern America', 'Middle East', 'Western Europe', 'Asiatic Region', 'Pacific Region', 'Latin America', 'Eastern Europe', 'Africa/Middle East', 'Africa'}
```

Q8 - Mean of H-index by region.

