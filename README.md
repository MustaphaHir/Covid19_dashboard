PROJET DASHBOARD

Voici le rendu de mon projet en Python, un dashboard représentant l'étude du COVID-19 dans le monde entre le 22 janvier 2020 et le 2 décembre 2020. Le jeu de données a été pris sur Kaggle.com. Voici le lien des données: https://www.kaggle.com/junyingsg/covid19-dataset.

USER GUIDE: 

Pour executer le code, on lance le fichier dash.app et installer certains packages via les commandes suivantes: Dash : pip install dash, Plotly-express : pip install plotly-express, Plotly : pip install plotly, Panda : pip install pandas. Suite à cela, le programme est prêt à être lancer, CTRL + F5 et cela va ouvrir une page HTML à l'URL http://127.0.0.1:8050/.

DEVELOPPER GUIDE:

Le code se divise en deux parties, la première partie consiste à déclarer les figures ainsi que les deux cartes pour le dashboard et la seconde partie où le dashboard est crée.

RAPPORT D'ANALYSE:

Le jeu de données contient 9 catégories "Date,Province/State,Country,Lat,Long,Confirmed,Recovered,Deaths,Active". Ce qui a permis de faire une répresentation graphique de la répartions des cas confirmés et aussi des cas décédés dans le monde.

![newplot](https://user-images.githubusercontent.com/93908318/147844579-d9d27e9f-4fa8-487c-ad44-b7b437268863.png)

Nous pouvons selectionner un pays, par exemple ici la France, pour y voir l'évolution des cas confirmés sur toute l'année.

![image](https://user-images.githubusercontent.com/93908318/147844727-0b6bc38a-8fcc-481d-af66-110a309c5d47.png)

![newplot (1)](https://user-images.githubusercontent.com/93908318/147844746-854f5a8a-bac7-481a-9333-7cbc8d200cb8.png)

Nous pouvons aussi voir le nombre de cas confirmés et décédés pour la France.

![image](https://user-images.githubusercontent.com/93908318/147844779-a5c23914-546a-4c32-91c4-7fa92209b78e.png)

![image](https://user-images.githubusercontent.com/93908318/147844790-3d81852f-f6d0-4681-a23e-9a6762cb3571.png)

Un graphique animé est présent afin de voir l'évolution des cas confirmés.

![newplot (2)](https://user-images.githubusercontent.com/93908318/147844800-c0a6971c-db94-4619-8144-ad39cd2db7d2.png)
