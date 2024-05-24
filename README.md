# Cloud-computing : Chiffrement et Dechiffrement en utilisant les cles de AWS

## Préparation de l'environnement 

![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/23.png)

![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/24.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/25.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/26.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/27.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/28.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/29.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/30.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/31.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/32.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/33.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/34.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/35.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/36.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/37.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/38.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/39.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/40.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/41.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/42.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/43.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/44.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/45.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/46.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/47.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/48.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/49.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/50.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/51.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/52.png)
## Création des clés et Utilisation
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/53.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/54.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/55.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/56.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/57.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/58.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/59.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/60.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/61.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/62.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/63.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/64.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/65.png)



# Cloud-computing : Deploiement d'une appli sur AWS

## Mise à jour du système

```sh
sudo apt-get update
```

## Installation de Python 3 et des outils nécessaires

Installez Python 3 et les outils nécessaires pour créer des environnements virtuels :

```sh
sudo apt-get install python3 python3-venv python3-pip -y
```

## Clonage du dépôt

Pour obtenir ce dépôt, lancez la commande suivante dans votre terminal compatible avec git :

```sh
git clone https://github.com/2liaepsi/Cloud-computing.git
```

## Création et activation d'un environnement virtuel

Pour isoler les dépendances de votre projet, créez un environnement virtuel :

### Création de l'environnement virtuel

Dans le répertoire du projet cloné, créez un environnement virtuel :

```sh
cd Cloud-computing
python3 -m venv venv
```

### Activation de l'environnement virtuel

Activez l'environnement virtuel avec la commande appropriée à votre système d'exploitation :

Pour Linux/macOS :

```sh
source venv/bin/activate
```

Pour Windows :

```sh
venv\Scripts\activate
```

## Installation de Django et NumPy

Avec l'environnement virtuel activé, installez Django et NumPy en utilisant pip :

```sh
pip install django numpy
```

## Configuration de l'application

Une fois que vous avez installé Django, allez dans le répertoire du dépôt cloné et exécutez les commandes suivantes :

```sh
cd Cloud-computing
ls -lrt
python3 manage.py makemigrations
```

Cela créera tous les fichiers de migrations nécessaires à l'exécution de cette application.

### Appliquer les migrations

Pour appliquer ces migrations, exécutez la commande suivante :

```sh
python3 manage.py migrate
```

## Création d'un utilisateur admin

Nous devons créer un utilisateur admin pour faire fonctionner cette application. Dans le terminal, tapez la commande suivante et fournissez le nom d'utilisateur, le mot de passe et l'email pour l'utilisateur admin :

```sh
python3 manage.py createsuperuser
```

## Démarrage du serveur

Démarrons le serveur pour mettre l'application en ligne. Utilisez la commande suivante :

```sh
python3 manage.py runserver
```

```sh
python3 manage.py runserver 0.0.0.0:8000
```
```sh
ls -lrt
cd appli_crypt
nano settings.py
```
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/1.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/2.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/3.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/4.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/5.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/6.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/7.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/8.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/9.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/10.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/11.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/12.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/13.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/14.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/15.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/16.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/17.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/18.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/19.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/20.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/21.png)
![Logo GitHub](https://github.com/2liaepsi/Cloud-computing/blob/main/1/22.png)

Une fois le serveur démarré, rendez-vous sur [http://127.0.0.1:8000/Cloud-computing](http://127.0.0.1:8000/Cloud-computing) pour accéder à l'application.

C'était assez simple, non ? Vous pouvez maintenant commencer à utiliser votre application !
