# Emotion_detection
Téléchargement de FER2013.csv :

```
pip install kaggle

```
https://www.kaggle.com/deadskull7/fer2013?select=fer2013.csv

# Contexte du projet

Les expressions du visage peuvent naturellement servirent à évaluer la satisfaction d’un client aux prises avec un service après-vente ou à face à un produit récemment acquis dont il s’agit de comprendre le fonctionnement. On peut encore mentionner les applications suivantes :

La détection d’un manque d’attention chez un conducteur en vue d’augmenter la sécurité de la conduite.
L’évaluation du niveau de stress de passagers à l’atterrissage ou à l’arrivé en gare ou la détection de comportements suspects.
L’humanisation des robots dans leurs interactions avec les humains dont ils prendraient en compte l’état psychique.


# Modalités pédagogiques

Le projet se fait en groupe (2 ou 3 personnes).

# Critères de performance

Le code doit bien être structuré, avec des explications sur le choix de l'architecture utilisée dans le modèle et une évaluation de la performance du modèle.

# Modalités d'évaluation

Un rapport sur le projet réalisé qui explique les différentes étapes du code

# Description des données

Présentation de l'architecture utilisée

Conclusion (avantages et inconvénients, concurrents, recommandations…)

Revue de code avec le formateur.

Après la finalisation du projet avec son rapport, une présentation ppt pourra être demandé des différentes étapes du projet, une explication du code et une demo.

# Livrables

- Un lien Github vers le code python de l'interface graphique. 

- Cette interface permet de reconnaitre l'émotion d'une personne à travers une image où bien une Webcam.

- Elle permet aussi d'associer un emoji qui représente l'émotion de la personne dans l'image/vidéo

- Finalement, elle va lui poser des questions si l'émotion est négative (ex. pourquoi es-tu triste, ...), si l'émotion est positive elle va la féliciter.

# Choix du modèle
Le CNN est idéal pour faire une classification d'image.
6 couches couches de convolutions
La convolution(Conv2D) est la première couche à extraire des entités d'une image d'entrée. La convolution préserve la relation entre les pixels en apprenant les caractéristiques de l'image à l'aide de petits carrés de données d'entrée.La convolution d'une image avec différents filtres peut effectuer des opérations telles que la détection des contours, le flou et la netteté en appliquant des filtres. Nous avons choisi la fonction d'activation Elu qui semble la plus efficace dans ce cas.
Avec une accuracy de 83 % , le choix de 7 couches avec ,sur la dernière couche, la fonction d'activation Softmax pour la classification semble vraiment un bon compromis.

# Lancement des applications

Installation:
```
pip install -r requirements.txt
```
Lancer:
```
streamlit run photo_detect_emotions.py

streamlit run webcam_detect_emotions.py

```

# Résultats

J'ai limité à 100 Epoch et j'ai obtenu une précision de 83 % pour le modèle.


![img1](./Emotion_img/2021-04-14-145430.png)
![img2](./Emotion_img/2021-04-14-145530.png)

![img4](./Emotion_img/2021-04-14-150018.png)
![img5](./Emotion_img/2021-04-14-150452.png)
