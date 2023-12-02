# 🖧 Preparació d'un entorn de desenvolupament amb Docker, part 1 🖧

Els primers dies ja vam muntar el nostre entorn amb Linux, l'entorn virtual...

Llavors, per a què muntem un altre entorn ? 

Perquè tenir un entorn aïllat amb Docker localment ens facilitarà molt la 
vida a l'hora de desplegar les nostres aplicacions web en un entorn remot.

# Creació del nostre entorn de treball amb Docker.

Primerament, hem de comparar Docker amb un programari que realitza operacions aparentment similars, que és VirtualBox, un un generador de màquines virtuals. 

També hi ha altres virtualitzadors com VMWare, QEMU.

### Comparativa VirtualBox vs Docker. 

| VirtualBox  | Docker      |
| :---        | :---        |
| - Programari emulat |  - Programari emulat |
|- SO emulat (o guest): Linux, Mac, Windows, Android, iOS ...| - SO emulat (o guest): Linux, Mac, Windows, Android, iOS ...|
|- Hardware emulat: VDI, RAM, ISO, ... |  - Hardware emulat: VDI, RAM, ISO, ... |
|- **Virtualizador:**  VirtualBox, VMWare, QEMU.|  - **Container Engine-> Docker Daemon**|
|- Sistema Operatiu (host): Linux, Mac, Windows, Android, iOS ... | - Sistema Operatiu (host): Linux, Mac, Windows, Android, iOS ...|
|- Hardware (host): 16 GB RAM, Intel / AMD processador   |- Hardware (host): 16 GB RAM, Intel / AMD processador | 

VirtualBox emula el hardware (les VDI, processadors, RAM ...) i això té un cost  considerable. 
<em>Un exemple típic: necessitem 2 nuclis de CPU i 6GB de RAM per la VM de Linux i almenys 2GB i 1 CPU per mantenir actiu el SO Host de Windows.</em> 

A diferència de VirtualBox, no hi ha una emulació a Docker; comparteixein el hardware del host.

Si tinc un processador amb 8 nuclis al meu PC, a Docker també els tenim, no n'hem de reservar pel SO host.

![[Docker vs VirtualBox]](containers-vs-virtual-machines.jpg)

## Què és són els contenidors de Docker ? 

Un contenidor (de Docker) és un procés aïllat. 
Està basat en el format **estàndard de contenidors de Linux (LXC)** i permet **córrer aplicacions en ambients aïllats de manera lleugera**; de la mateixa manera que en 
el **transport de mercaderies s'utilitzen contenidors amb un tamany estàndard**
independentment del que portin.

Per això, el logo de docker és una balena que porta contenidors a sobre (com un vaixell).

Gràcies a compartir el mateix hardware (el mateix vaixell), Docker és més ràpid i consumeix menys memòria (tant de RAM com de disc dur).

<hr/>

## Usos principals de Docker.

- Deployment. Sobre com desplegar aplicacions en servidors web(PHP,MySQL,...) ho veureu a altres mòduls. 

- Development. És en el que ens centrarem en aquests apunts.

L'avantatge d'usar Docker en el Deployment és que ja no cal instal·lar els serveis web: Apache, PHP, MySQL.

També aporta flexibilitat si volem canviar versions d'aquests programes (de PHP 7 a 8) o a programes similars (usar MariaDB en comptes de MySQL)

Un segon avantatge és que ens assegurem que els serveis i el programari que usen els coincideix

Evitem el meme: "a la meva màquina funciona".

![[Meme: a la meva màquina funciona]](https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd)


### Programari que necessitem per usar Docker.

- Docker Desktop -> Ens oblidem, és una escurabutxaques com WinRAR.

És programari privatiu.

- **Docker Engine -> Ës el sistema que usarem.** 

És FOSS -> Free and Open Source Software.

#### Pàgina oficial.

[https://docs.docker.com/get-docker/]

www.docker.com -> Docs -> Download and Install

No usarem exactament els passos que proposa la pàgina. Usarem els següents:

Obrim terminal d'Ubuntu, sense entorn virtual per ara:

```sh
box@m14$ sudo apt update
box@m14$ sudo apt install docker.io
box@m14$ sudo apt install docker-compose
```

El docker-compose no l'usarem per ara però ens vindrà bé quan tinguem molts contenidors i volguem orquestrar-los (decidir en quin ordre s'executen i com interactuen entre ells). 
També hi ha Kubernates que és més avançat, si voldeu ser un perfil devops (dev+admin)

A les últimes versions d'Ubuntu (i PopOS) es diu docker compose.

### Permisos necessaris per a usar Docker com a developers.

Primer, hem d'assignar-nos el grup de docker (que s'ha creat automàticament a l'instal·lar docker) al nostre usuari.

```sh
sudo usermod -aG docker $USER
```

Per provar que s'ha aplicat el canvi de grup:
```sh
sudo /etc/group | grep docker
docker:x:1000:box,miquel
```

L'any que es va crear la Shell de Unix, també es van crear aquestes variables d'entorn ($USER,$PATH...), que avui en dia s'usen en tots els sistemes operatius. Unix també va ser impulsor dels SO multiusuari.

#### Provem si s'ha instal·lat Docker:

```sh
systemctl status docker
```

Resultat esperat:

```sh
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2022-12-16 17:18:59 CET; 10min ago
TriggeredBy: ● docker.socket
```

Mirem que s'ha creat el daemon de docker.

- **Daemon** -> Procés del sistema, que s'executa en segon pla (background)

L'equivalent de Windows són els serveis.

### Tipus comandes a Docker.

- Options
- Management
- Commands.

Usem les management commands; són més fàcils de recordar i d'aprendre.

De builder fins a volume.

Moltes són semblants a Git, per facilitar la integració amb aquest.

## Definicions importants a Docker.

### Image.

Ârbre de fitxers i directoris comprimits que contenen tot el que necessita el meu entorn.
Les **imatges son només de lectura.**
Les guardarem al nostre PC, amb un sistema de fitxers especial. 
Analogia: Semblant al codi instal·lable d'un programa.

Opcions de docker image:
```sh
docker image --help
```

### Contenidor.

**Procés aïllat que s'executa a partir de una imatge.** Així obtenim més seguretat (no afectarà al sistema si cau un contenidor)
Analogia: Un procés de qualsevol sistema, que és un programa en execució.

A priori són també de lectura; per garantir estabilitat. Es podria escriure per configurar-lo.
També estan preparats per a ser reiniciats fàcilment si els contenidors cau.

Podem arrencar i parar un contenidor quan vulguem.

Opcions de docker image:
```sh
docker container --help
```

#### Exemples: 

- Entorn amb Apache, PHP i MySQL.
- Entorn amb Python, Pandas, Flask i Biopython.


## On obtenim imatges ja fetes ?  

De DockerHub. [Provem cercar una imatge de Flask a Dockerhub, per a fer aplicacions web amb Python](https://hub.docker.com/search?q=flask)

Una altra opció semblant és Django; però per ara Flask està creixent molt amb popularitat.

El Laravel és el framework de generació de págines web amb PHP. Per generar pàgines web automàtiques amb Python tenim Flask i Django.  

Triem la segona:
- rapidfort/flaskapp

Docker Official Image => Feta pels de docker amb versions estables.

## Muntem una imatge.

Busquem hello-world i agafem la primera

https://hub.docker.com/_/hello-world

No agafem la comanda per defecte de Dockerhub, fem la comanda management:

docker image pull hello-world

```sh
(base) mamorosal@pop-os:~$ docker image pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
2db29710123e: Pull complete 
Digest: sha256:c77be1d3a47d0caf71a82dd893ee61ce01f32fc758031a6ec4cf1389248bb833
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```

**Tag:** La versió. Si surt **lastest** és que és la última versió.

**Hash:** És un codi que conté la firma que idenfifica un usuari de forma segura en un servidor. En aquest cas usa l'algoritme d'encriptació amb SHA256. Té el més important d'un fitxer.

Per entendre-ho, quan fem commit a Git des del terminal surt el codi de Hash.

## On està la imatge ?

Apliquem la comanda docker image ls

```sh
(base) mamorosal@pop-os:~$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    feb5d9fea6a5   14 months ago   13.3kB
```

## Com arrenquem el contenidor ? 

docker container run nom_de_la_imatge

```sh
(base) mamorosal@pop-os:~$ docker container run hello-world

Hello from Docker!

This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

☺☺ Enhorabona, ja hem arrencat el nostre primer programa amb Docker. ☺☺

⚠ Observació. La paraula podem fer **docker run** en comptes de docker container run

Per exemple, si volem descarregar-nos i arrencar la imatge del projecte bio-kekule (que desplega un servei web al port 80) creat pel David de Mingo ho fariem així

```sh
docker run --rm -d --name kekule -p 80:80 registry.gitlab.com/xtec/bio-kekule
```

Gitlab inclou un servei que et permet administrar imatges de docker; una alternativa vàlida a dockerhub. 
Més info a:
https://docs.gitlab.com/ee/user/packages/container_registry/

I Github també:
https://docs.github.com/es/packages/working-with-a-github-packages-registry/working-with-the-docker-registry


## <a href="../Docker2/readme.md"> Accedeix a la pròxima sessió, on seguim muntant imatges de Docker més potents :) </a>

<hr/>
