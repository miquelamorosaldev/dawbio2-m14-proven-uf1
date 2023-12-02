# MP014 - Bioinformàtica.
<br/>

Per compartir més fàcilment la teoria i exemples curs, anem publicant en aquests documents compartits:

<a href="https://docs.google.com/document/d/1X-RTtJr6zzcd5WIBLuB50iACn0aA0MpwZEs_ZGhtuEI/edit">DAWBIO-14 - Bioinformàtica</a>

També podeu trobar els projectes resolts des dels comptes:

* https://github.com/miquelamorosaldev/

* https://gitlab.com/xtec/

En aquesta pàgina només mantenim actualitzades les primeres sessions.

### 🖧 Preparació d'un entorn de desenvolupament amb Docker 🖧

Hem muntat l'entorn i les imatges necessaries el dia 04/12/2023:

1. [Conceptes previs, instal·lació de Docker i el nostre primer contenidor](./Docker_s1)
2. [Creem més contenidors de Docker](./Docker_s2)


## UF1 - Informàtica mèdica. Apunts i exemples 2023 - 2024.

### Sessió 1 - Preparació entorn local: SO Linux, Python, venv i editor VSCode.

Podem muntar l'entorn de treball de 2 maneres semblants:

#### Op1. RECOMANADA. Una instal·lació d'una màquina virtual de Linux amb VirtualBox i ús del VSCode a Windows.

Aquesta opció <a href="https://docs.google.com/document/d/1q8HR7pqQf4RTePXK9fe7Q-ywn-COaPI4M1mXEn-Y-PQ/edit#heading=h.v2vgeymgts4e">la exposem pas a pas per aplicar-la aquest curs 2023-2024 en un Doc.Compartit</a>

La pàgina oficial del projecte que usem és https://box.xtec.dev/

- ✅ L'avantatge de la primera opció és que no cal gastar-se un euro i podem aprofitar el SO Windows per les  tasques que consumeixen més recursos (VSCode) i la màquina virtual de Linux com a servidor. Si tenim un ordinador de gama mitjana o alta (>8GB RAM i processador modern) es treballa bé així. ✅
- ⚠ L'únic inconvenient és que heu de repetir els passos o clonar la màquina i portar-la a casa, les FCT (a no ser que allí ja tingueu Linux) ⚠

#### Op2. Una instal·lació de Linux nativa dins d'un disc dur SSD extraible. 

Aquesta opció <a href="./UF1_A01_Ses1_PreparacioEntornConda">la vam usar en cursos anteriors en aquesta wiki</a>


- ✅  L'avantatge de la segona opció és que només cal aplicar els passos un sol cop, i ja podem emportar-nos tot el sistema a l'institut, a casa, a les FCT i on volguem. És útil per aprofitar les prestacions del PC. ✅
- ⚠ L'inconvenient és que cal fer una inversió econòmica i de temps. ⚠

#### Op3. Usar el WSL (Windows Subsystem for Linux). Ideal si som un usuari/a adminstrador/a.

Seguiu el tutorial:

https://www.arsys.es/blog/wsl-windows-subsystem-linux 

I apliqueu aquesta comanda a la Windows PowerShell:

```powershell
wsl --install
```

En qualsevol cas recomanem que useu Python i Linux i exposarem les 3 maneres.

### 🐍 Sessió 1 - Repàs funcionalitats bàsiques de Python. 🐍

Pressuposem que ja s'han treballat les funcions, bones pràctiques i estructures bàsiques de Python, i aquí en fem un repàs.
La resta de recursos queden com a referència. 
- Introducció Bàsica a Python 
- print
- condicions i bucles
- llistes, list comprension
- diccionaris
- Tuples
- Slices
- Conjunts (Sets)
- Ajuda

Podeu triar el format de document que preferiu (no cal els 2, són molt semblants)

[Repàs Python, format wiki](./A012_RepasPythonPart1 "Repàs Python, part 1")

[Repàs Python, format JupyterNotebook](https://colab.research.google.com/drive/1axvXnQdWhBTO-zTcv_mI6_cK30XPpj3v?authuser=0#scrollTo=XZShFCsbUcVj&uniqifier=1)

<hr/>

### Sessió 2.1 - Programació OO i Funcional amb Python.

[Documentació i codi font](./UF1_S02_POO_Func)

### Sessió 2.2 - Exercicis explotació de dades de fitxers CSV amb Python.

[Documentació i codi font](./UF1_S02_CSV_Scimago)

### Sessió 3 - Testing i control versions sobre les consultes al fitxer CSV Scimago.

[Documentació i codi font](./UF1_S03_Scimago_Tested)

### Sessió 4 - Arrays de Numpy i series de Pandas.

[Documentació i codi font](./UF1_S04_Numpy)

### Sessió 5 - Pandas: Series i Dataframes.

[Documentació i codi font](./UF1_S05_Pandas1)

### Sessions posteriors (de la 6 a la 9)

Per tal d'agilitzar la documentació s'ha optat per seguir un document compartit 
indexat, que inclou enllaços als nostres repositoris de git.

[🗎 Documentació i codi font en Docs.Compartits](https://docs.google.com/document/d/1X-RTtJr6zzcd5WIBLuB50iACn0aA0MpwZEs_ZGhtuEI/edit)

<hr/>

### Introducció a les API's amb Flask (sessions 10 - 12)

Es troben en els mateixos docs. compartits.

[🗎 Documentació i codi font en Docs.Compartits](https://docs.google.com/document/d/1X-RTtJr6zzcd5WIBLuB50iACn0aA0MpwZEs_ZGhtuEI/edit)

També recomanem consultar els següents repositoris:

💻 Exemple web plantilla amb serveis web Flask.
https://gitlab.com/xtec/flask

💻 Exemple web plantilla amb Flask i la llibreria de gràfics i mapes Plotly.
https://gitlab.com/xtec/plotly

💻 Projecte pràctic 2. Web amb Flask, gràfics i mapa.
https://github.com/miquelamorosaldev/dawbio2-pt2-template-flask

💻 Possible solució del projecte 2.
https://github.com/miquelamorosaldev/dawbio2-pt2-solution

<hr/>
