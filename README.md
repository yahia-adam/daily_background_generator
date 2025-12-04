# 🎨 **Daily Background Generator — Wallpapers IA Quotidiens**

## 📌 **Description**

Daily Background Generator est une application intelligente qui génère automatiquement des fonds d'écran artistiques uniques chaque jour en utilisant l'IA générative. Le système combine des styles de grands maîtres (Van Gogh, Monet, Picasso, Dalí…) avec des sujets variés (paysages, portraits, scènes urbaines…) pour créer des œuvres d'art originales qui sont automatiquement définies comme fond d'écran sur votre bureau GNOME.

Le projet fusionne **génération d'images par IA**, **automatisation système** et **art classique** pour offrir une expérience visuelle renouvelée quotidiennement.

**Clicker pour voir la vidéo démo :**

[![Demo](https://img.youtube.com/vi/cS7cVoVBsfc/0.jpg)](https://youtu.be/cS7cVoVBsfc "Demo Video")

---

## 🎯 **Objectif du projet**

* Générer quotidiennement des wallpapers artistiques uniques et personnalisés.
* Combiner l'art classique (grands maîtres) avec l'IA générative moderne.
* Automatiser le processus de création et d'application des fonds d'écran.
* Offrir une expérience visuelle dynamique sans intervention manuelle.
* Explorer les capacités créatives de Stable Diffusion 3.

---

## 🧠 **Contexte & Problématique**

Les fonds d'écran statiques deviennent monotones avec le temps. Changer manuellement son wallpaper régulièrement demande du temps et de la recherche d'images de qualité.

Daily Background Generator résout ce problème en :

* **générant automatiquement** des œuvres d'art uniques chaque jour,
* **variant les styles artistiques** pour maintenir la fraîcheur visuelle,
* **appliquant le fond d'écran automatiquement** sans intervention manuelle,
* **créant de l'art original** plutôt que de recycler des images existantes.

---

## 🏗️ **Architecture du pipeline**

1. **Génération de prompts**

   * Sélection aléatoire d'un style artistique parmi 8 grands maîtres.
   * Choix aléatoire d'un sujet parmi 8 catégories.
   * Construction d'un prompt détaillé avec instructions artistiques.
   * Génération d'une description unique combinant style + sujet.

2. **Génération d'image par IA**

   * Chargement du modèle Stable Diffusion 3 Medium.
   * Traitement avec PyTorch en float16 (optimisation mémoire).
   * 28 étapes d'inférence pour équilibrer qualité/vitesse.
   * Guidance scale de 7.0 pour suivre fidèlement le prompt.

3. **Sauvegarde et nommage**

   * Enregistrement au format PNG.
   * Nommage basé sur la date du jour (un seul wallpaper par jour).
   * Stockage dans un répertoire dédié.

4. **Application système**

   * Utilisation de gsettings (GNOME Desktop).
   * Définition automatique comme fond d'écran.
   * Intégration transparente avec le système.

5. **Automatisation**

   * Planification via cron pour exécution quotidienne.
   * Aucune intervention manuelle requise.

---

## 🛠️ **Technologies utilisées**

**Modèle IA :**

* Stable Diffusion 3 Medium (Stability AI)

**Framework Deep Learning :**

* PyTorch 2.4.0 (avec support CUDA 12)
* Diffusers 0.30.0 (Hugging Face)
* Transformers 4.44.0

**Accélération GPU :**

* NVIDIA CUDA 12 (cublas, cudnn, cufft, curand, cusolver, cusparse)
* Triton 3.0.0

**Traitement d'images :**

* Pillow 10.4.0

**Calculs numériques :**

* NumPy 1.26.4

**Intégration système :**

* OS module (commandes shell)
* gsettings (paramètres GNOME)

**Authentification :**

* Hugging Face Hub 0.24.5

**Utilitaires :**

* datetime (timestamps)
* random (sélection aléatoire)
* tqdm 4.66.5 (barres de progression)

---

## 📚 **Compétences mobilisées**

### **IA Générative**

* Text-to-Image avec Stable Diffusion
* Prompt Engineering avancé
* Optimisation de modèles (float16, inference steps)
* Guidance scale tuning

### **Deep Learning**

* PyTorch
* Pipelines de diffusion
* Gestion mémoire GPU
* Inférence optimisée

### **Automatisation Système**

* Scripts Python automatisés
* Intégration avec GNOME Desktop
* Tâches cron
* Gestion de fichiers système

### **Design & Art**

* Connaissance des styles artistiques
* Composition visuelle
* Théorie des couleurs et textures

---

## 🚀 **Fonctionnalités principales**

* Génération de prompts artistiques combinant 8 styles × 8 sujets = 64 combinaisons possibles.
* Création d'images uniques via Stable Diffusion 3 Medium.
* Application automatique comme fond d'écran GNOME.
* Un seul wallpaper par jour (évite la duplication).
* Support GPU NVIDIA pour génération rapide.
* Prompt engineering intégré (brushstrokes, textures, impasto).
* Totalement automatisable via cron.

---

## 📂 **Structure du projet**

```
/daily_background_generator
├── app.py                  # Script principal
├── requirements.txt        # Dépendances Python
├── README.md              # Documentation
├── .gitignore             # Fichiers ignorés par Git
└── /images                # Wallpapers générés
    ├── 2025-01-15.png
    ├── 2025-01-16.png
    ├── ...
    └── merged.mp4         # Démo vidéo
```

---

## ▶️ **Installation & Exécution**

### 1. Cloner le projet

```bash
git clone git@github.com:yahia-adam/daily_background_generator.git
cd daily_background_generator
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Se connecter à Hugging Face

```bash
huggingface-cli login
```

Suivez les instructions pour vous connecter avec vos identifiants Hugging Face.

### 5. Configuration

Modifiez les constantes dans [app.py](app.py) si nécessaire :

```python
GET_SETTING_PATH = "/usr/bin/gsettings"  # Chemin vers gsettings
SAVE_IMAGE_PATH = "/home/votre_utilisateur/daily_background_generator/images"
```

### 6. Exécution manuelle

```bash
python3 app.py
```

### 7. Automatisation quotidienne

Pour exécuter automatiquement tous les jours à minuit :

```bash
crontab -e
```

Ajoutez la ligne suivante :

```bash
0 0 * * * /chemin/vers/.venv/bin/python /chemin/vers/daily_background_generator/app.py
```

---

## 📊 **Exemples de résultats**

### Prompt généré

> "a mysterious forest in the style of Vincent van Gogh. Swirling brushstrokes, bold colors, and dramatic textures. Emphasize thick impasto and expressive, energetic brushwork. Capture the essence of Vincent van Gogh's emotional and dynamic approach."

### Image créée

Une forêt mystérieuse avec :

* Coups de pinceau tourbillonnants caractéristiques de Van Gogh
* Couleurs vives et audacieuses
* Textures épaisses (impasto)
* Énergie émotionnelle et dynamique

### Application

* Fichier : `/images/2025-01-15.png`
* Résolution : Adaptée au modèle SD3 Medium
* Fond d'écran : Appliqué automatiquement sur GNOME

---

## 🎨 **Galerie**

![Exemple 1](https://raw.githubusercontent.com/yahia-adam/daily_background_generator/main/images/1.webp)

![Exemple 2](https://raw.githubusercontent.com/yahia-adam/daily_background_generator/main/images/3.webp)

---

## 🧪 **Configuration technique**

### Styles artistiques disponibles

* Vincent van Gogh (Post-Impressionnisme)
* Claude Monet (Impressionnisme)
* Pablo Picasso (Cubisme)
* Jackson Pollock (Expressionnisme abstrait)
* Frida Kahlo (Surréalisme)
* Salvador Dalí (Surréalisme)
* Georgia O'Keeffe (Modernisme américain)
* Edvard Munch (Expressionnisme)

### Sujets disponibles

* Paysages vibrants
* Portraits sereins
* Scènes urbaines animées
* Paysages marins tranquilles
* Compositions abstraites
* Ciels nocturnes dramatiques
* Scènes de rue vivantes
* Forêts mystérieuses

### Paramètres de génération

```python
num_inference_steps=28      # Équilibre qualité/vitesse
guidance_scale=7.0          # Force du prompt
torch_dtype=torch.float16   # Optimisation mémoire GPU
negative_prompt=""          # Sans restrictions
```

---

## 🔧 **Dépannage**

### Erreur d'authentification Hugging Face

```bash
huggingface-cli login
```

Assurez-vous d'avoir accepté les conditions d'utilisation de Stable Diffusion 3 sur le hub Hugging Face.

### Problème de chemin gsettings

Vérifiez que gsettings est installé :

```bash
which gsettings
```

Mettez à jour `GET_SETTING_PATH` dans [app.py](app.py) avec le bon chemin.

### Erreur de permissions

Assurez-vous d'avoir les droits d'écriture dans `SAVE_IMAGE_PATH` :

```bash
chmod +w /chemin/vers/images/
```

### Mémoire GPU insuffisante

Le modèle utilise déjà `torch.float16`. Si vous avez encore des problèmes :

* Fermez les autres applications utilisant le GPU
* Réduisez `num_inference_steps` (ex: 20 au lieu de 28)
* Utilisez un GPU avec plus de VRAM

### Le fond d'écran ne change pas

Vérifiez que vous utilisez GNOME Desktop :

```bash
echo $DESKTOP_SESSION
```

Pour d'autres environnements (KDE, XFCE…), la commande `gsettings` doit être adaptée.

---

## 🚀 **Améliorations futures**

* Support multi-environnements (KDE, XFCE, Windows, macOS)
* Interface graphique pour choisir styles et sujets
* Historique des wallpapers générés avec galerie
* Mode haute résolution (4K, 8K)
* Intégration de styles artistiques personnalisés
* Mode "série" (plusieurs images d'un même style)
* API REST pour génération à distance
* Application mobile compagnon

---

## 📖 **Prérequis système**

* **OS** : Linux avec GNOME Desktop (Ubuntu, Fedora, Debian…)
* **Python** : 3.8+
* **GPU** : NVIDIA avec support CUDA 12 (recommandé)
* **RAM** : 8 GB minimum
* **VRAM** : 6 GB minimum (GPU)
* **Stockage** : 10 GB pour le modèle + images
* **Compte** : Hugging Face (gratuit)

---

## 👤 **Auteur**

**YAHIA ABDCHAFEE Adam**

---

## 📄 **Licence**

Ce projet est open source. Consultez le dépôt pour les détails de licence.

---

## 🤝 **Contribution**

Les contributions sont les bienvenues !

* Ouvrez une issue pour signaler un bug
* Proposez une pull request pour ajouter des fonctionnalités
* Partagez vos wallpapers générés dans les discussions

---

## 🔗 **Liens utiles**

* [Stable Diffusion 3 Medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium-diffusers)
* [Hugging Face Diffusers](https://huggingface.co/docs/diffusers)
* [PyTorch Documentation](https://pytorch.org/docs)
* [GNOME gsettings](https://docs.gtk.org/gio/class.Settings.html)

---

## 📈 **Performances**

* **Temps de génération** : ~30-60 secondes (avec GPU NVIDIA)
* **Qualité d'image** : Haute résolution, artistiquement cohérente
* **Consommation mémoire** : ~6 GB VRAM GPU
* **Stockage par image** : ~2-5 MB (PNG)

---

**Transformez votre bureau en galerie d'art dynamique avec Daily Background Generator !** 🎨✨
