# Training-Data

## Description

**Training-Data** est un projet ETL (Extract, Transform, Load) développé en Python. Il permet d'extraire des données depuis une base MySQL, de les transformer puis de les recharger dans les tables cibles.

Le projet est organisé de manière modulaire afin de séparer clairement les étapes d'extraction, de transformation et de chargement.

---

## Structure du projet

```text
training-data/
│
├── database/
│   └── ... données sources
│
├── scripts/
│   ├── __init__.py
│   │
│   └── ETL/
│       ├── __init__.py
│       ├── extract.py
│       ├── transform.py
│       └── load.py
│
├── workflows/
│   ├── __init__.py
│   └── manip.py
│
├── __init__.py
├── pipeline.py
├── requirements.txt
└── SQL_ANALYSIS.ipynb
```

---

## Description des composants

### database/

Contient les données sources utilisées pour les traitements ETL.

### scripts/ETL/

Ce répertoire regroupe les différentes étapes du pipeline :

#### extract.py

Responsable de l'extraction des données depuis la base MySQL.

#### transform.py

Contient les opérations de nettoyage et de transformation des données :

* conversion de types ;
* création de colonnes calculées ;
* préparation des données avant chargement.

#### load.py

Responsable du chargement des données transformées dans les tables cibles.

### workflows/

Contient les fonctions utilitaires utilisées par le pipeline.

#### manip.py

Fonctions de manipulation et de traitement utilisées par les étapes ETL.

### pipeline.py

Point d'entrée principal du projet.

Il exécute successivement :

1. l'extraction ;
2. la transformation ;
3. le chargement.

---

## Technologies utilisées

* Python
* MySQL
* Pandas
* SQLAlchemy
* MySQL Connector
* PyYAML
* Jupyter Notebook

---

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/votre-utilisateur/training-data.git
cd training-data
```

Créer un environnement virtuel :

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Dépendances

Le projet utilise les bibliothèques suivantes :

```text
pandas
sqlalchemy
mysql-connector-python
pyyaml
jupyter
```

---

## Exécution du pipeline

Pour exécuter le traitement ETL complet :

```bash
python pipeline.py
```

---

## Analyse des données

Le notebook `SQL_ANALYSIS.ipynb` permet :

* d'explorer les données ;
* de tester les requêtes SQL ;
* de valider les transformations ;
* d'effectuer des analyses exploratoires.

---

## Flux de traitement

```text
MySQL
   │
   ▼
extract.py
   │
   ▼
transform.py
   │
   ▼
load.py
   │
   ▼
Tables cibles
```

---

## Auteur

Projet réalisé dans le cadre d'un apprentissage de l'ingénierie des données, des pipelines ETL et de la manipulation de données avec Python et MySQL.
