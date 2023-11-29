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

## Récupérer les fichiers

### Avec git : cloner le répertoire

Si vous voulez suivre les mises à jour des paquets plus facilement, et pour contribuer,  vous pouvez le cloner avec git installé: dans un terminal, dans le dossier où vous voulez le cloner:

`git clone https://github.com/redclem/anki-union <dossier destination>`

Maintenant tous les fichiers sont disponibles dans le nouveau dossier, qui est géré par git.
Notamment, dans le répertoire cloné:

- Pour mettre à jour:

`git pull origin main`

- Pour voir quels fichiers ont été mis à jour par rapport à la version précédente:

`git diff --name-only HEAD@{1}`

#### Sans git

- Naviguer vers le fichier qui vous intéresse

![](https://github.com/Redclem/Anki-Union/blob/main/README_data/download_screen_0.png?raw=true)

- Télécharger avec "download raw file"

![](https://github.com/Redclem/Anki-Union/blob/main/README_data/download_screen_1.png?raw=true)

## Importer dans Anki

#### Première fois

Si vous importez des paquets pour la première fois, vous devez importer les types de notes spéciaux utilisés. En plus des decks que vous voulez, vous devez importer le paquet "card_types.apkg"

### Anki sur ordinateur

- Fichier > Importer
- Naviguer jusqu'au fichiers à importer

### Ankidroid

Pas possible d'importer des csv sur Ankidroid pour l'instant. Je recommande de créer un compte ankiweb et de synchroniser Anki entre votre ordinateur et votre téléphone.




