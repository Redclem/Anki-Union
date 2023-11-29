# Anki-Union

Merci à tous ceux qui ont contribué, même si ce n'est qu'en signalant des erreurs!

Des paquets anki sympas.
Plus précisément :
- Paquets de langue généraux (plus de modifications)
- Citations des oeuvres au programmes de Français prépa scientifiques 22/23
- Paquets de première année MP2I (incomplets : manque fondamentaux et bases d'analyse, plus de modifications sauf corrections éventuelles)
- Paquets de seconde année MPI (assez complets, plus de modifications sauf corrections éventuelles)
- L3 Informatique ENS Lyon + Algèbre 1 + Mesure et Intégration + Double licence maths UCBL (Notes complémentaires à celles des cours de mathématiques de l'ENS)

Les paquets sont sous format csv, car le format apkg n'apporte pas de gain de taille, et le csv permet un meilleur usage avec git.
Vous pouvez importer les types de notes avec le paquet "Card Types" qui contient des cartes vides.

Si vous avez besoin d'aide, envoyez un message sur discord : redclem (le renard).

# Importer les paquets

2 OPTIONS : Les fichiers csv ou apkg

- Les fichiers csv contiennent toutes les dernières mises à jour mais doivent être importés avec anki sur ordinateur.
- Les paquets apkg sont plus simples à utiliser mais seront mis à jour moins souvent



## Fichiers .csv

### Récupérer les fichiers avec git : cloner le répertoire

Si vous voulez suivre les mises à jour des paquets plus facilement, et pour contribuer,  vous pouvez le cloner avec git installé: dans un terminal, dans le dossier où vous voulez le cloner:

`git clone https://github.com/redclem/anki-union <dossier destination>`

Maintenant tous les fichiers sont disponibles dans le nouveau dossier, qui est géré par git.
Notamment, dans le répertoire cloné:

- Pour mettre à jour:

`git pull origin main`

- Pour voir quels fichiers ont été mis à jour par rapport à la version précédente:

`git diff --name-only HEAD@{1}`

### Récupérer les fichiers sans git

- Naviguer vers le fichier qui vous intéresse

![](https://github.com/Redclem/Anki-Union/blob/main/README_data/download_screen_0.png?raw=true)

- Télécharger avec "download raw file"

![](https://github.com/Redclem/Anki-Union/blob/main/README_data/download_screen_1.png?raw=true)

## Importer dans Anki

#### Première fois

Si vous importez des paquets pour la première fois en .csv, vous devez importer les types de notes spéciaux utilisés. En plus des decks que vous voulez, vous devez importer le paquet "card_types.apkg"

Si vous avez déja importé des notes de ce type en paquets apkg, pas besoin!

Dans le doute, importez le petit paquet card_types.

### Anki sur ordinateur

- Fichier > Importer
- Sélectionner les fichiers à importer


- Ne rien toucher ! Sauf si vous savez ce que vous faites. Appuyez juste sur le bouton "Importer" tout mignon
![](https://github.com/Redclem/Anki-Union/blob/main/README_data/import_screen.png?raw=true)

### Ankidroid

Pas possible d'importer des csv sur Ankidroid pour l'instant. Je recommande de créer un compte ankiweb et de synchroniser Anki entre votre ordinateur et votre téléphone.

Utilisez les apkg fournis en release

## Paquets apkg

### Télécharger les paquets

Ils sont disponibles dans "Releases" sur la page du git (celle où vous êtes probablement). Téléchargez le zip et extrayez les paquets qu'il vous faut.

## Importer

L'importation devraît se faire facilement sur ordinateur et Ankidroid

- Sur ordi : Fichier > Importer
- Ankidroid : Les trois points en haut à droite > Importer

# Bon Courage !

Vous devez désormais être armés pour réviser ! Soyez réguliers et restez motivés !
