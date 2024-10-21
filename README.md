# Qu'est ce que c'est ?

MonitorServices est un logiciel permettant de monitorer  
des services webs
si un service est down, alors l'évenement
est signalé sur la page web du serveur


# Instructions pour utiliser le service


## 1. vérifier si python3 est installé
```
$> python3 -V
Python3 3.10.*
```
ou si ça ne fonctionne pas

```
$> python -V
Python3 3.10.*
```

## 2. si python n'est pas installé faire l'installation
```
sudo apt install python3
```

## 3. installer flask  
`$> pip3 install flask`


## 4. Pour télécharger par zip

<details> <summary> par zip </summary>

fichier zip téléchargeable par ce lien depuis un navigateur

https://github.com/whoamitty/MonitorServices/archive/refs/heads/main.zip


Pour télécharger et décomprésser le zip depuis un terminal

```
cd ~/chemin/vers/la/ou/on/veut/mettre/le/dossier

wget https://github.com/whoamitty/MonitorServices/archive/refs/heads/main.zip

unzip MonitorServices-main.zip -d dossier_de_destination

rm MonitorServices-main.zip #pour supprimer le zip
```
</details>



## 5. Pour télécharger par git
<details> <summary> par git </summary>
Si le compte github auquel est lié git as accès au depo  
ses commandes permettent de télécharger le depo en local


### 5.1 installer git (pour vérifier `git --version`)
`$> sudo apt install git`


### 5.2 télécharger le depo

```
git clone --depth=1 git@github.com:whoamitty/MonitorServices.git dossier_du_depo
```

`dossier_du_depo` sera créé dans le dossier courant

si `dossier_du_depo` n'existe pas, le dossier `dossier_du_depo` seras créé par git  

si aucun nom de dossier est donnée
le nom du dépo `MonitorServices` sera choisi par défault
</details>





## 6. ce placer dans le dossier du code
`$> cd ~/chemin/vers/le/dossier_du_depo`

ou si le dépo est dans le répertoire courant

`$> cd dossier_du_depo`

## 7. Pour lancer le serveur, exécuter:

`$> python main.py`
la base de donnée `./mydata.db` seras automatiquement créé


## 8. l'adresse du serveur seras affiché

Example:
```
$> python main.py
2.6.0
table table_service already exists
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
```



## 9. Pour changer le port et l'IP du serveur  
modifier les constantes suivantes dans le fichier des constantes constant.py :
```
PORT="8000"
IPSERVERFLASK="127.0.0.1"
```

## 10. Vous pouvez aussi y modifier ces constantes:  
```
MAXTRIES=3 #nombre d'éssais consécutifs échoués maximum avant de classer le serveur en indisponible  
WAIT=300 # temps d'attente entre chaques essais en secondes
```

## 11. Pour modifier les données  
vous pouvez utiliser un logiciel de gestion de base de données(comme sqlit_web),  
ou vous inspirer du code dans `managedbUser.py`


## 12. Le fichier de base de donnée `./mydata.db`  
seras automatiquement créé en  
important le module `constant`

