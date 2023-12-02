# 🖧 Preparació d'un entorn de desenvolupament amb Docker, part 2 🖧

Avui investigarem i provarem algunes de les imatges que disposa DockerHub per muntar un contenidor amb un entorn de desenvolupament (Python, PHP...)

⚠ Les carpetes que pengen (configs,pathlib,flask) les utilitzem a la última part d'aquesta sessió. ⚠

Al final de la sessió 1 vam muntar un HelloWorld. Repassem:
- Imatge: Fitxers i directoris comprimits que contenen tot el necessari.
- Contenidor: Procés aïllat 
- Virtualitzador: Compartim el Hardware i el Sistema Operatiu del Host.

## Imatges de dockerhub.

#### ⚠ De cara a muntar un projecte de final de grau, us pot anar molt bé trobar un DockerHub que contingui el sistema operatiu Ubuntu o similar i el programari necessari (Python,SQL,...) 

DockerHub:
https://hub.docker.com

Important mirar la informació de les imatges.
- Tag: La versió. Si surt **lastest** és que és la última versió.

## Historial dels contenidors arrencats.

Ho hem de fer amb aquesta comanda, per mostrar tots els contenidors arrencats:
docker container ls -a

```sh
(base) mamorosal@pop-os:~$ docker container ls -a
CONTAINER ID   IMAGE                COMMAND                  CREATED      STATUS                    PORTS     NAMES
ebb885dcb2bf   rapidfort/flaskapp   "/bin/sh -c 'uwsgi -…"   2 days ago   Exited (30) 2 days ago              practical_wu
b251529948c0   hello-world          "/hello"                 2 days ago   Exited (0) 2 days ago               bold_meitner
```

Els NAMES que assigan Docker són aleatoris.
El COMMAND és important:

Podem veure més opcions:

```sh
(base) mamorosal@pop-os:~$ docker container ls --help

Usage:  docker container ls [OPTIONS]

List containers

Aliases:
  ls, ps, list

Options:
  -a, --all             Show all containers (default shows just running)
```

Podem posar el nostre nom de contenidor:

```sh
docker container run hello-world -name green-donatello
```


### Eliminar contenidors

**Prune** -> Els elimina tots.
Però guarda l'estat dels contenidors per si volem tornar-lo a aixecar en una altre sessió.


```sh
(base) mamorosal@pop-os:~$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
b96422344b6e5906ef57b7a0b068d17f4ba1d655cc9d1b9610136333fa2804cb
ebb885dcb2bf33c6776a84458f4e30cc1260c2f2d1d7dc17bf4e8909366b2ef0
b251529948c031f93955d6c7e3e00f14814dae561768f8834e63420b92e2e5d5
Total reclaimed space: 148.4kB
(base) mamorosal@pop-os:~$ docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Baixem una distro de Linux amb Docker.

Fedora, Ubuntu, Alpine (muy ligera, ideal per a deployment)

Però com a developers, triem Ubuntu, ens la descarreguem:

```sh
(base) mamorosal@pop-os:~$ docker image pull ubuntu 
Using default tag: latest
latest: Pulling from library/ubuntu
6e3729cf69e0: Already exists 
Digest: sha256:27cb6e6ccef575a4698b66f5de06c7ecd61589132d5a91d098f7f3f9285415a9
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

Si volem, podem eliminar la imatge de hello-world:

```sh
(base) mamorosal@pop-os:~$ docker image rm hello-world:latest
Untagged: hello-world:latest
Untagged: hello-world@sha256:c77be1d3a47d0caf71a82dd893ee61ce01f32fc758031a6ec4cf1389248bb833
Deleted: sha256:feb5d9fea6a5e9606aa995e879d862b825965ba48de054caab5ef356dc6b3412
Deleted: sha256:e07ee1baac5fae6a26f30cabfe54a36d3402f96afda318fe0a96cec4ca393359
```

Ja no podrem crear més contenidors amb aquesta imatge :( ens la hauriem de tornar a baixar.


### Arrenquem la distro d'Ubuntu

Abans, mirem quina versió de PopOS tenim:

```sh
(base) mamorosal@pop-os:~$ uname -a
Linux pop-os 5.17.5-76051705-generic #202204271406~1653440576~22.04~6277a18 SMP PREEMPT Wed May 25 01 x86_64 x86_64 x86_64 GNU/Linux
```

Ara, arrenquem un contenidor d'Ubuntu amb la imatge descarregada. Ocupa molt menys que una ISO.

Què vol dir -it --> 2 paràmetres: -i Interactive - t terminal

```sh
(base) mamorosal@pop-os:~$ docker container run -it ubuntu bash
root@c8c6f009ed71:/# 
```

**Enhorabona, hem entrat com root :D**

Fixeu-vos que el nostre container utilitza el Kernel del Host:

```sh
root@c8c6f009ed71:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@c8c6f009ed71:/# uname -a
Linux c8c6f009ed71 5.17.5-76051705-generic #202204271406~1653440576~22.04~6277a18 SMP PREEMPT Wed May 25 01 x86_64 x86_64 x86_64 GNU/Linux
root@c8c6f009ed71:/# 
```

### Instal·lar programes al nostre contenidor.

Hem de fer un update abans que res.

```sh
root@c8c6f009ed71:/# nano    
bash: nano: command not found
root@c8c6f009ed71:/# sudo apt install nano
bash: sudo: command not found
root@c8c6f009ed71:/# apt update
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [114
.....
```sh

Ara ja podem instal·lar i usar programes amb l'apt

```sh
apt install nano
.....
nano
```

Recordeu que per sortir de nano es Ctrl+X, Ctrl+O guardar.

Instal·lem més coses:
```sh
apt install tree
nano
```

### Parem i reiniciem el contenidor.

Parem contenidor amb una de les 2 opcions:

Ctrl + D 
o 
Exit + INTRO

Veiem l'historial:

```sh
(base) mamorosal@pop-os:~$ docker container ls --all
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                          PORTS     NAMES
c8c6f009ed71   ubuntu    "bash"                   38 minutes ago   Exited (0) About a minute ago             modest_yalow
872b974adb0d   ubuntu    "bash -name ubuntu22…"   38 minutes ago   Exited (1) 38 minutes ago                 peaceful_elion
18eb0948f45e   ubuntu    "-name ubuntu22amoros"   42 minutes ago   Created                                   quirky_antonelli
```

### Com reanudem un contenidor parat ? 

#### Opció 1. 
Amb aquestes comandes el reanudem, però esta corrent en segon pla (background)

```sh
(base) mamorosal@pop-os:~$ docker container start modest_yalow
modest_yalow
(base) mamorosal@pop-os:~$ docker container ls --all
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS     NAMES
c8c6f009ed71   ubuntu    "bash"                   41 minutes ago   Up 31 seconds                         modest_yalow
872b974adb0d   ubuntu    "bash -name ubuntu22…"   41 minutes ago   Exited (1) 41 minutes ago             peaceful_elion
18eb0948f45e   ubuntu    "-name ubuntu22amoros"   46 minutes ago   Created                               quirky_antonelli
```

Faltaria la commanda per posar-lo en primer pla, attach:
```sh
(base) mamorosal@pop-os:~$ docker container attach modest_yalow
root@c8c6f009ed71:/#
```

#### Opció 2.

Les 2 anteriors comandes les podem resumir en aquesta:

```sh
(base) mamorosal@pop-os:~$ docker container start -a modest_yalow
```

### Com parar un contenidor des de fora del terminal.

És molt important, si tanquem accidentalment el terminal o per tancar bé la sessió de Linux.

```sh
(base) mamorosal@pop-os:~$ docker container stop -t 1 modest_yalow
```

**-t** ==> Número de segons abans de tancar.


### Eliminar contenidors.

Només podem eliminar contenidors parats.

```sh
(base) mamorosal@pop-os:~$ docker container rm modest_yalow
```

### Tornar a arrencar contenidor eliminat.

Ctrl+R al terminal -> cerquem la comanda a l'historial.

```sh
docker container run -it ubuntu bash
```

Penseu que s'ha eliminat tot el contingut que teníem abans; torna a l'estat que tenia a l'iamtge. 


## Com podem crear una imatge pròpia del meu contenidor ? 

Amb el commit, com github.

```sh
(base) mamorosal@pop-os:~$ docker container commit tender_austin bio:v1
sha256:36959837ed46a3303977ab65af744bd9a8b7495b6036402a1ebc8c42c536386b
```

Ens surt un hash, l'id de la imatge.

Provem que ha funcionat :) 

```sh
docker container run -it bio:v1 bash
```

Ara, podriem instal·lar els programes que necessitem: Python, Jupyter, Pandas....

Fins i tot ho podriem automatitzar amb un fitxer .sh

Però molt millor usar imatges amb tot el programari configurat.



# Com muntar un entorn de BioPython automàticament ? 

Podem utilitzar un fitxer dockerfile que contingui tots els passos que volem automatitzar.
Us donem un fitxer ja fet.

## Creem un contenidor amb el codi que teniu dins les carpetes.

Mirem el fitxer:

[./0-configs/1-docker/dev.Dockerfile]

On tenim comandes no interactives que ens permeten instal·lar automàticament tot el necessari.

**-y** -> No ens cal confirmar res.

Fixeu-vos com automatitzem la instal·lació de tot el necessari per programar amb Python 3:

```code
# Basic system utilities
RUN apt-get install -y dialog nano tree zip git sqlite3 curl lynx

# Python packages. python3 is already installed but write it for completeness.
RUN apt-get install -y python3 python3-venv python3-pip python-is-python3
```

### I Conda ? El necessitem o no ? 

Amb Docker, no necessitem Conda, perquè ja tenim l'entorn aïllat (que és el que fa Conda en en nostre entorn de Pandas, Seaborn...)

La altra funció de Conda és instal·lar llibreries, però tenim altres alternatives famoses com **pip** i/o **venv** per aquest propòsit.

Amb tot, per garanitzar la seguretat, creem un entorn virtual dins el contenidor i hi inclourem Python:

```code
ENV VIRTUAL_ENV=/opt/bio-venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
```

Curiositats:

/opt/ ---> Carpeta on instal·lar els nostres propis paquets 

La tercera línia és l'equivalent al "conda activate bio"

## Construim el contenidor.

Usem la comanda: 
**docker image build --tag bio --file dev.Dockerfile .**

```sh
(base) mamorosal@pop-os:~/Documents/0-configs$ docker image build --tag bio --file dev.Dockerfile .
Sending build context to Docker daemon   7.68kB
Step 1/15 : FROM ubuntu
 ---> 6b7dfa7e8fdb
Step 2/15 : ENV DEBIAN_FRONTEND noninteractive
 ---> Running in 29501aac4011
Removing intermediate container 29501aac4011

....

 ---> a947c077c180
Successfully built a947c077c180
Successfully tagged bio:latest
--file dev.Dockerfile
```

Punts importants:

* image build 
* --tag bio
* --file dev.Dockerfile
* . (és important, indica que volem usar els fitxers de la mateixa carpeta)

Al cap de 2-3 minuts (amb una bona connexió) ja ho tenim tot instal·lat.

Ja podriem començar.

**Funciona:**

```sh
root@6251c0c6584d:/# python
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> list1=[5,6,2,7]
>>> list1
[5, 6, 2, 7]
```

Si voleu instal·lar llibreries, usem la pàgina de pip:

https://pypi.org/project/pip/

Solen ser comandes del tipus:
pip install <library>

Una altra comprovació:

echo $PATH

Tindreu les variables d'entorn necessaries.

#### Llistat de llibreries que instal·lem automàticament

Les tenim dins del fitxer: 

<a href="./0-configs/1-docker/requirements.txt">./0-configs/1-docker/requirements.txt</a>


### Carpeta compartida per interactuar des del Host amb el Docker.

Primer, heu de crear una carpeta del vostre disc que sigui localitzable. Heu de copiar la ruta absoluta.

```sh
docker container run -it --name bio --mount=src='/home/mamorosal/Documents/docker-code',target='/bio',type='bind', bio bash
```

Comentaris:
Nom imatge == Nom Contenidor
El mount és super important que sigui exacte, és el que crea la carpeta compartida, l'src és la ruta de la carpeta del disc, i el target de la carpeta compartida dins de Docker.

Comprovem-ho:

1. Apliquem la comanda. 
2. Posem un fitxer .txt dins de la carpeta del host
3. Fem un ls dins del contenidor de docker, dins la carpeta /bio
4. Fixem-nos que funciona.

Tingueu en compte que heu d'estar com a root dins de docker.

```sh
(base) mamorosal@pop-os:~/Documents/0-configs$ docker container run -it --name bio --mount=src='/home/mamorosal/Documents/docker-code',target='/bio',type='bind' bio bash
root@6251c0c6584d:/# ls
bin  bio  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@6251c0c6584d:/# cd bio
root@6251c0c6584d:/bio# ls
Instalar-Sessio1m14.txt
```

### FAQ'S 1. No em funciona Python dins la carpeta compartida.

Es deu a un problema de permisos.
Dins del docker, canvieu els permisos d'usuari:

```sh
sudo chown -R <usuari>:<usuari> .
```

### FAQ'S 2. No em reconeix l'entorn de Python /opt/venv.

A alguns equips no reconeix una carpeta que hauria de reconèixer a VSCode, la que hi ha l'entorn virtual:
**/opt/bio-venv/bin/python**

El que farem és crear un entorn nou igual a l'anterior, per a què el VSCode el reconegui,

```sh
root@39afbdb94c74:/bio# which -a python
/opt/bio-venv/bin/python
/usr/bin/python
/bin/python
root@39afbdb94c74:/bio# /bin/python -m venv bio-env2
root@39afbdb94c74:/bio# ls
2023-01-09-code  bio-env2
root@39afbdb94c74:/bio# cd bio-env2/
root@39afbdb94c74:/bio/bio-env2# ls
bin  include  lib  lib64  pyvenv.cfg
root@39afbdb94c74:/bio/bio-env2# cd ..
root@39afbdb94c74:/bio# cd bio-env2/bin/
root@39afbdb94c74:/bio/bio-env2/bin# ls
Activate.ps1  activate  activate.csh  activate.fish  pip  pip3  pip3.10  python  python3  python3.10
root@39afbdb94c74:/bio/bio-env2/bin# source activate.
activate.csh   activate.fish  
root@39afbdb94c74:/bio/bio-env2/bin# source activate
(bio-venv) root@39afbdb94c74:/bio/bio-env2/bin# source activate
(bio-venv) root@39afbdb94c74:/bio/bio-env2/bin# which -a python
/opt/bio-venv/bin/python
/opt/bio-venv/bin/python
/usr/bin/python
/bin/python
```

Un cop seguides aquestes instruccions ja ens deix seleccionar l'entorn virtual.

És especialment important: 
```sh
source activate
```

Un cop ha reconegut l'entorn; necessitarem instal·lar-hi les llibreries.

La forma més fàcil és usar el fitxer requirements.txt que tenim a la carpeta de docker:

```sh
pip install -U requirements.txt
```

## Com treballar amb Docker i VSCode? 

Extensions a instal·lar a VSCode:
- Docker
- Dev Containers

Us sortiran noves icona a sota: 
- Docker -> forma de balena.
- Dev Containers > Forma pantalla. 

![[Captura dels plugins de VSCode que gestionen els nostres contenidors de Docker]](Docker-VSCoder.png)

### Resultat final 

Arrencant aquests plugins aconseguim arrencar/parar i accedir a la carpeta compartida on tenim el contenidor amb el VSCode.

![[Captura de la carpeta compartida del contenidor ja muntada i accessible des de  VSCode]](Docker_VSCode_Full.png)

<hr/>
<hr/>

<a name="Sessió3_Debug" > </a>

# Com treballem amb Docker ?

Hem repassat tot el que vam fer:
- Teoria de Docker: imatges i contenidors 
- Crear un contenidor d'Ubuntu a partir d'una imatge de DockerHub
- Crear un contenidor d'Ubuntu i totes les eines de Python preparades mitjançant 
- Crear una carpeta compartida entre el contenidor docker i el nostre SO Host.
- Gestionar el contenidor i la carpeta compartida des de VSCode.

## Com executar i debugar un codi Python/Flask/PHP... independentment de la carpeta

Els projectes de VSCode tenen una carpeta oculta amb la configuració de debug (entre d'altres) del projecte.
Podeu consultar-la amb **ls -la** des del terminal o amb **Ctrl+F8** des del explorador gràfic

Es troba a:
<projecte>
  .vscode 
    launch.json

Esborreu aquesta carpeta i podreu crear una configuració de debug personalitzada.

La podeu generar amb VSCode, que és el més recomanable.

Aneu al botó de Debug i us sortirà el següent; pitgeu a crear Launch.JSON

![[Captura del botó de Debug]](Launch_JSON.png)

### Més informació del launch.json 

La teniu en aquests apunts, per a què recordeu com es fa ? 

<a href="./docker-howto.md">howto.md</a>

Recurs opcional:

https://towardsdatascience.com/how-to-debug-flask-applications-in-vs-code-c65c9bdbef21


### I que passa si no volem usar VSCode ? 

Usarem el fitxer **no_interpreter.py**

<a href="./no_interpreter.py">no_interpreter.py</a>

Aquest fitxer serveix per a fer que no sigui obligatori trobar-nos a la mateixa carpeta on està el fitxer Python per a poder executar el fitxer. 
Compleix la mateixa funció del launch.json per si no useu VSCode.

