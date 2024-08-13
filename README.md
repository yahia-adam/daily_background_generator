# Daily Background Generator

> Daily background generator: Créez des wallpapers uniques pour chaque jour de la semaine.

Ce projet développe un programme qui génère automatiquement un nouveau fond d'écran artistique unique pour chaque jour de la semaine. En utilisant l'API Stable Diffusion, il crée des images personnalisées inspirées par des styles de grands maîtres tels que Van Gogh, Monet, ou Picasso, combinés à des sujets variés allant de paysages vibrants à des compositions abstraites. Ces créations sont ensuite appliquées dynamiquement comme fond d'écran du PC, offrant une expérience visuelle qui mêle art classique et technologie moderne, renouvelée quotidiennement.

[![Demo](https://img.youtube.com/vi/cS7cVoVBsfc/0.jpg)](https://youtu.be/cS7cVoVBsfc "Demo Video")

## Prérequis

- Python 3.x
- Un compte Hugging Face
- Un système Linux avec GNOME Desktop

## Installation

### Cloner le dépôt

Commencez par cloner le dépôt sur votre machine locale :

```bash
git clone git@github.com:yahia-adam/daily_background_generator.git
cd daily_background_generator
```

### Créer un environnement virtuel Python

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Installer les dépendances du projet

```bash
pip install -r requirements.txt
```

### Se connecter à Hugging Face

```bash
huggingface-cli login
```

Suivez les instructions pour vous connecter avec vos identifiants Hugging Face.

## Configuration

Avant d'utiliser le script, assurez-vous de modifier les constantes suivantes dans le code :

- `GET_SETTING_PATH` : le chemin de la commande `gsettings`
- `SAVE_IMAGE_PATH` : le chemin où vous voulez stocker les images générées

Exemple :

```python
GET_SETTING_PATH = "/usr/bin/gsettings"
SAVE_IMAGE_PATH = "/home/adam/adam/daily_background_generator/images"
```

## Utilisation

## Fonctionnement

1. Le script génère une image à l'aide de l'API Stable Diffusion.
2. L'image générée est sauvegardée dans le dossier spécifié par `SAVE_IMAGE_PATH`.
3. La fonction `set_background()` est appelée pour définir cette image comme nouveau fond d'écran.

## Exécution

Pour exécuter le script :

```bash
python3 app.py
```

## Automatisation

Pour exécuter ce script automatiquement, vous pouvez configurer une tâche cron. Voici un exemple pour l'exécuter tous les jours à minuit :

1. Ouvrez votre crontab : `crontab -e`
2. Ajoutez la ligne suivante :

    ```bash
    0 0 * * * /chemin/vers/votre/env/python /chemin/vers/votre/app.py
    ```

## Dépannage

- Assurez-vous que vous êtes bien connecté à Hugging Face.
- Vérifiez que les chemins `GET_SETTING_PATH` et `SAVE_IMAGE_PATH` sont corrects pour votre système.
- Assurez-vous que vous avez les permissions nécessaires pour écrire dans le dossier de sauvegarde des images et pour exécuter `gsettings`.

## Contribution

Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Auteur

YAHIA ABDCHAFEE Adam


![day1](https://raw.githubusercontent.com/yahia-adam/daily_background_generator/main/images/1.webp)
![day3](https://raw.githubusercontent.com/yahia-adam/daily_background_generator/main/images/3.webp)

Daily background generator: Create unique wallpapers for each day of the week.
