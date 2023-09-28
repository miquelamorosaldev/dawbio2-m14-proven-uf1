# Session 3. Scimago CSV queries solved and tested.

Volem realitzar diverses consultes sobre la base de dades Simago (scimago-main-queries.py)
, per organitzar articles científics per tipus, per factors d'impacte com l'H-index o el número de citacions, per
país o regió, categories ...

Al final de resoldre les consultes, hem verificat la seva validesa amb tests de Pytest, comparant els resultats que esperem amb els resultats reals de la funció (scimago-test-queries.py)


### [Document testing i control de versions.](https://docs.google.com/document/d/1zeyi1DW5lCKWQOVrcpZyyi9WMUiQpQy0y6l-HRo5VU4/edit)


## Q1 - How many entries are in scimago-medicine.csv?

```python
for entry in entries:
	entry['Country'] == 'Spain'
```

#### Q1 - Expected result (in 2022):
7251

## Q2 - Show the first 25 entries.

## Q3 - How many entries are from Spain? (Country = Spain)

Hint Q3:
```python
for entry in entries:
	entry['Country'] == 'Spain'
```

#### Q3 - Expected result (in 2022):
137


## Q4 - Show all the journals (Type = journal) published in UK (Country = United Kingdom) with an 
H-Index greater than 200, sorted by H-index (biggest H-Index first)

Hint:
https://stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python

## Q5 - What types of scientific publications are in the file (paràmetre Type)?

#### Q5 - Expected result:
```python
['journal', 'book series', 'conference and proceedings', 'trade journal']
```

## Q6 - Count the number of types of each scientific publication.

```python
{'journal': 7082, 'book series': 27, 'conference and proceedings': 5, 'trade journal': 4}
```

## Q7 - Show all regions covered by all entries.

Hint; expected result:
```python
{'Northern America', 'Middle East', 'Western Europe', 'Asiatic Region', 'Pacific Region', 'Latin America', 'Eastern Europe', 'Africa/Middle East', 'Africa'}
```

## Q8 - Mean of H-index by region.

