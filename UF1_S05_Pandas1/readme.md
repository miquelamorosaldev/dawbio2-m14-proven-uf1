# Sessió 5 - Pandas 1

Seguirem  un document compartit on publicar en directe el que fem:

https://docs.google.com/document/d/1t1CfE5HERkWI4AsWsW4XVGidY084AP4jOV5uVUCRchc/edit

Aquest repositori no té tots els exemples, però són curts i estan al document compartit.

Si que conté instruccions bàsiques de com arrencar-los.

### Instal·lacio Pandas: 

Definim el nom del nostre entorn i que volem instal.lar Pandas (també inclou Numpy i Matplotlib).

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 -m pip install --upgrade pip
(.venv) $ pip install pandas
```

Les primeres llibreries a importar son dues:

 · **np** --> Numpy, llibreria per a realitzar càlculs numèrics
 · **pd** --> Llibreria Pandas, per a gestionar i analitzar dades tabulars indexades.

```python
import numpy as np 
import pandas as pd
```

 Panda utilitza dos tipus dades bàsics:
 1. **Series** , estructura 1D que s'assembla a una llista.
 2. **DataFrame**, estructura 2D que presenta les dades com una taula, o en definitiva un conjunt de Series.
 
  ### Series
  
  #### pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
  
  **Referència:** [Doc.Oficial Series de Pandas.](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
  
  Té diversos paràmetres d'entrada, dels quals 3 són els principals:
  
    1. **data.** Ha de cubrir tots els possibles continguts de la sèrie. Habitualment se li passa una llista plena.
    2. **dtype** Contingut dels valors de les dades. Inicialment tots del mateix tipus.
    3. **index.** L'índex el pots configurar al teu gust. Per defecte és numèric, però podem elegir d'un altre tipus segons el cas.

## DTYPE. Tipus de dades que s'utilitzen a Pandas.

 ·**dtype** = Data Type. Es un camp que utilitza la llibreria NumPy.
   Numpy utilitza el seu propi tipus, codificats al llenguatge de programació C, per eficiència. 
   
  *Exemple: float 64(bits), int 64(bits), "string", datetime*
  
```python
ser = pd.Series([1, 3, 5, np.nan, 6, 8])
print(ser)
```

*Sortida*

>   0    1.0
>   
>   1    3.0
>   
>   2    5.0
>   
>   3    NaN
>   
>   4    6.0
>   
>   5    8.0
>   
>   dtype: float64


### Tractament dades indeterminades o inexistents. 

Dins del contingut indeterminat, hi ha 3 conceptes diferents en Numpy (i Pandas=:

   ·**NaN**: Not a Number (infinit, Indeterminar). La dada està calculada. Concepte matemàtic.
   
   ·**NA**:  Not Avalaible (No disponible). La dada no hi és, no existeix. Concepte estadístic.
   
   ·**None**:  És un objecte que fa el mateix que NA. No és eficient, millor usar NA.

Per eficiencia a *Python* i *Pandas* s'utilitza NaN quant vol dir NA.

Podem esborrar la dada np.nan o bé ignorar-la; més endavant veurem què és millor fer en cada cas.

Si son uniformes el dtype tria el tipus de dades correcte i més adient.

Una serie es pot forçar a un tipus de dades prefixat per nosaltres.

```python
ser = pd.Series([1, 3, 5, 6, 8], dtype=np.float32)
print(ser)
```

 >   0    1.0
 >   
 >   1    3.0
 >   
 >   2    5.0
 >   
 >   3    6.0
 >   
 >   4    8.0
 >   
 >   dtype: float32
 >   


## Creació de sèries amb Pandas.

Provem el següent codi:

```python
import numpy as np 
import pandas as pd
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
works_fct_list = [False,True,False,True]
ser = pd.Series(grades_list)
print(ser)
```

>    0    7
> 
>    1    9
> 
>    2    8
> 
>    3    4
> 
>    dtype: int64
>    

Per defecte, la sèrie assigna un index autonumèric.

Les sèries de Pandas també es poden crear amb indexs propis (poden ser strings, dates...)

```python
#index canviats a índex d'estudiants
ser = pd.Series(data=grades_list,index=student_list)
print(ser)
```

 >   John     7
 > 
 >   Mary     9
 >
 >   Lucy     8
 >
 >   Peter    4
 >
 >   dtype: int64


Per a consultar quins dtype té cada serie del dataframe, usem el mètode **.dtypes** 

```python
print(ser.dtypes)
```

 >  grade           int64
 >  
 >  works_fct             bool
 >  
 >  cat_grade    category
 >
 >  dtype: object

**Referència**
[Guia completa de tipus de dades DTYPE, web oficial NumPy](https://numpy.org/doc/stable/reference/arrays.dtypes.html)

## DataFrame

Podem seguir l'exemple del tutorial [en aquest punt](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#object-creation "aqui")

**Codi d'exemple pd.Dataframe a classe**
[intro_pandas_dataframes.py](./intro_pandas_dataframes.py)

**Exemple 1: Dataframe d'informació d'animals.**

```python
import numpy as np
import pandas as pd

# Test dataframes
# Podem convertir un diccionari que els seus valors siguin llistes en un Dataframe.
dict_animals = {'num_legs': [2, 4, 0, 8], 'num_wings': [2, 0, 0, 0]}
# Com en les sèries, el valor dels índex el podem passar com una llista.
name_animals = ['falcon', 'dog', 'snail', 'spider']
df_animals = pd.DataFrame(data=dict_animals, index=name_animals)
print(df_animals)
```

Proveu l'exemple, i a veure si podeu inserir algún animal més.

**Exemple 2:** Com poder crear un dataframe a partir de 6 mesos diferents

![](dataframe.png)

Un altra forma de crear datasets, es nombrar totes les columnes i ficar la seva llista respectiva, que es mostrarà d'aquesta forma.

![](dataframe2.png)

**Una excepció diferent a Java, al final veieu que hi ha una coma, que amb Java donaria error, al python l'obvia i no li fa cas**

**Exemple 3:** Dataframe de diversos tipus de dades.

En aquest dataframe, podem modificar alguna serie, exemple la A, de tal manera que tingui alguns valors de tipus diferents.

Fixeu-vos en els resultats i codi de cada columna del Dataframe: usant diversos trucs hem aconseguit un Dataframe de 
6 columnes (camps) i 4 fileres (registres).

Fixeu-vos que cada fila del dataframe és una serie, a la columna "C" es pot comprovar:

```python
df3 = pd.DataFrame(

    {

        "A": [1.0] + [np.nan] * 3,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)
df3
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>


## Altres tipus de dades de Pandas.

### Categorical

```python
gender = pd.Categorical(["Male", "Female", "Non-Binary", "Transgender", "Intersex", "I prefer not to say"])
```

Categories (6, object): ['Female', 'I prefer not to say', 'Intersex', 'Male', 'Non-Binary', 'Transgender']

**Referència:** 
[How to ask about gender in forms respectfully](https://www.ruth-ng.co.uk/how-to-ask-about-gender-in-forms-respectfully)


### Timestamp
Serveix per a convertir enters en dates, per defecte en format americà.

```python
pd.Timestamp("20130102")
```

Timestamp('2013-01-02 00:00:00')


## Cheatsheet instruccions bàsiques.

A partir del exemple creat per nosaltres, amb les notes dels estudiants de DAWBIO que estan FCT, veurem les principals funcions del dataframe.

<a name="dataframe"></a>

Tenim varies llistes indiviFCTs, que al final formaran un sol dataframe:

```python
#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
works_fct_list = [False,True,False,True]
datos: dict[list] = {"grade": grades_list,
      "works_fct": works_fct_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
print(students_frame)
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="dtypes"></a>


```python
# Amb aquesta instruccio obtenim el tipus  de dades de cadascuna de les columnes.
students_frame.dtypes
```
    grade    int64
    FCT      bool
    dtype: object

## Funcions bàsiques de Pandas.

<a name="head"></a>

### Mostrar les primeres línies

```python
#Obtenir les primeres 5 linees de la taula
students_frame.head()
```

```python
# Les primeres 2 files
students_frame.head(2)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="tail"></a>

### Mostrar les últimes línies

```python
# Les últimes 2 files
students_frame.tail(2)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>

<a name="shape"></a>

### Mostra el número de files i columnes del dataframe.

```python
students_frame.shape()
```

**Resultat:**
(4, 2)

### Mostrem l'índex i les columnes.

```python
# Recupera el index (row names) i les columnes (column names)
# Atenció! No son funcions son atributs
print(type(students_frame.index))
```
    <class 'pandas.core.indexes.base.Index'>

<a name="describe"></a>

### Realitza càlculs estadístics.

Si el dataframe o la sèrie conté dades numèriques, obté càlculs estadístics: mitjana, moda, quartils... només de les columnes amb valors numèrics.

```python
students_frame.describe()
```

**Resultat:**
```
          grade
count  4.000000
mean   7.000000
std    2.160247
min    4.000000
25%    6.250000
50%    7.500000
75%    8.250000
max    9.000000
```

Es pot fer sobre tot el dataframe o únicament per una columna=camp.

<a name="sample"></a>

### Linea aleatòria

```python
# Linea aleatoria
students_frame.sample()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>

<a name="T"></a>

### Trasposar la matriu del dataframe

```python
students_frame.T
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>John</th>
      <th>Mary</th>
      <th>Lucy</th>
      <th>Peter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>grade</th>
      <td>7</td>
      <td>9</td>
      <td>8</td>
      <td>4</td>
    </tr>
    <tr>
      <th>FCT</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



**Codi d'exemple**
[intro_pandas_dataframes.py](./intro_pandas_dataframes.py)


<a name="sort_index"></a>

### Ordenació dataframes.

#### Ordenació dataframes per un índex

```python
#Ordenació per index axis=0 el index de la primera columna, axis=1 ordena els index de la primera columna (FCT,grade)
students_frame_sorted = students_frame.sort_index(axis=1, 
                                                  ascending=True)
students_frame_sorted
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>FCT</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>False</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>True</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>False</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>True</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>


<a name="sort_values"></a>

####  Ordenació dataframes per valors de columnes.

```python
#Ordenació per valors axis=0 columnes 
students_grade_sorted = students_frame.sort_values(by=['grade'], 
                                                   axis=0, 
                                                   ascending=False)
students_grade_sorted
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="coordenades"></a>

### Sistema coordenades de Dataframes. Consultes.

Amb un dataframe, el sistema de coordenades, comença per 0, i la coordenada s'indica primera la fila i després la columna.

**Regla nemotècnica (enfonsar-se i nedar)**

1. Primer et tires de cap a la posició de la fila que vols.

2. Llavors vas nedant fins la columna que t'interessa.
 
La funció més habitual per fer-ho és loc. 

Sintaxi general:

<em><strong>dataframe.loc [ --fila o llista de files-- , --columna o fila de columnes -- ] </em></strong>


<center>
 
 <img src="dive-jump.gif" alt="dive jump" width="300"/>

</center>

```python
# Utilitzar sempre localització d'un atribut
# .loc rep 2 parametres('enfonsar-se','bucejar')
students_frame.loc["Lucy","grade"]
```
>  8

<a name="loc"></a>


#### Cerca de varis valors en diferentes columnes.

```python
#busqueda de mes d'una columna
students_frame.loc["Lucy",["grade","FCT"]]
```

    grade        8
    FCT     False
    Name: Lucy, dtype: object


#### Cerca tots els valors d'una fila (element, registre)

```python
#si vull totes les columnes de Lucy fico un slice buit a la columna
students_frame.loc["Lucy",:]
```

    grade        8
    FCT     False
    Name: Lucy, dtype: object


#### Cerca tots els valors d'una columna (camp)

```python
#si vull totes les notes dels estudiants, a la fila poso un slice buit
students_frame.loc[:,"grade"]
```

    John     7
    Mary     9
    Lucy     8
    Peter    4
    Name: grade, dtype: int64

#### Cerca valor per fila i columna, iloc.

Ja hem utilitzat la funció **loc** , ficant el nom directament de les files primer i les columnes després. 
Amb les coordenades numèriques, hem d'anomenar el primer numero per columna i el segon per files.


```python
#La primera coordenada capbusada | i despres bucejo -> però amb numèrics.
students_frame.iloc[0,1]
```


    False


#### Comandes at, iat; optimització loc e iloc.

```python
#Les comandes at e iat son sinònimes de loc e iloc, però sol poden retornar un sol valor.
#at es una optimització

students_frame.at["Lucy","grade"]
```

>  8

```python
students_frame.iat[2,0]
```

>  8

#### Cerca llista de diverses files.

```python
#Podemos devolver una lista de varias filas, devuelve una lista
students_frame.loc[["Mary","Lucy"],"grade"]
```

>    Mary    9
>    Lucy    8
>    Name: grade, dtype: int64



```python
type(students_frame.loc[["Mary","Lucy"],"grade"])
```


>    pandas.core.series.Series



```python
#Podem retornar una llista de varies files, i retorna una llista
students_frame.loc[["Mary","Lucy"],
                   ["grade","FCT"]]
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>


```python
students_frame.loc[students_frame.index,["grade","FCT"]]
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


```python
#Mètode per seleccionar totes les files i columnes.
students_frame.loc[:,:]
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



```python
#No es recomanable, ficar el interval de columnes, encara que es pot fer
students_frame["John":"Lucy"]
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>fct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>


<a name="mask"></a>

#### Introducció al filtratge per Masks

Referència:
[Index and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html?highlight=mask)

```python
# Mask = Objecte que amaga tota la informació que no volem

students_pass = students_frame.loc[:,"grade"] >= 5
#Creo mask amb estudiants que compleixen criteris
students_pass
```

>    John      True
>    Mary      True
>   Lucy      True
>   Peter    False

>   Name: grade, dtype: bool


```python
#A la mascara anterior puc indicar per que seleccioni, sols els de la mask
students_frame.loc[students_pass,:]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>FCT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



```python
#sinonim
students_frame.loc[[True,True,True,False],:]
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>fct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>

<a name="sort"></a>

## Ordenació dataframes.

#### Ordenació per índex.

```python
#Ordenació per index axis=0 el index de la primera columna, axis=1 ordena els index de la primera columna.
dataframe_sorted = students_frame.sort_index(axis=1, ascending=True)
```
Si l'índex és un text l'ordenarà alfabèticament, si és un número de major a menor (o la inversa si ascending=False)...

#### Ordenació per valors de columnes.

```python
#Ordenació per valors axis=0 columnes i pel camp indicat dins del by.
students_grade_sorted = students_frame.sort_values(by=['grade'], axis=0, ascending=False)
#També és vàlida aquesta instrucció
students_grade_sorted = students_frame.sort_values(['grade'],ascending=False)
```

<a name="exercicis">

## Exercicis Pandas.

1. Crea un nou dataframe similar als dels alumnes, que tingui 4 - 6 files més (10 està bé) i 1 o 2 columnes més (per exemple: gènere, població)
2. L'index ha de ser el nom de l'alumne. Apart de ser índex també ha de ser un camp.
3. Mostra la mitjana de notes de tots els alumnes.
4. Ordena els alumnes alfabèticament.
5. Mostra tota la info d'un alumne, a partir del seu nom.
6. Mostra les notes dels 3 alumnes que tenen una nota més alta.
7. Usant una màscara, mostra els noms dels alumnes que volen fer FCT.
8. Usant una màscara, mostra els alumnes que tenen una nota superior o igual a 7.
9. Espai per a que creis 2 consultes i les seves solucions, a partir de les noves consultes que has creat.

<a name="sol_exercicis">

Podeu trobar les solucions fetes a classe al link:
  
[Exercicis Sessió5 Dataframes](./exercicisSessio5dataframes.py)
