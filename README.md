# Cloud-computing

## Mise à jour du système

```sh
sudo apt-get update
```

## Clonage du dépôt

Pour obtenir ce dépôt, lancez la commande suivante dans votre terminal compatible avec git :

```sh
git clone https://github.com/2liaepsi/Cloud-computing.git
```
## Installation de Django

Vous aurez besoin de Django installé sur votre ordinateur pour exécuter cette application. Rendez-vous sur [le guide de téléchargement de Django](https://www.djangoproject.com/download/) pour plus d'informations.

### Télécharger Django en utilisant pip

```sh
sudo apt install python3-pip -y
pip install django
```

## Configuration de l'application

Une fois que vous avez téléchargé Django, allez dans le répertoire du dépôt cloné et exécutez la commande suivante :

```sh
cd Cloud-computing
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

Une fois le serveur démarré, rendez-vous sur [http://127.0.0.1:8000/Cloud-computing](http://127.0.0.1:8000/Cloud-computing) pour accéder à l'application.

C'était assez simple, non ? Vous pouvez maintenant commencer à utiliser votre application todo !
