# LLM Agent - Financial Data Extractor 

Un outil Python robuste conçu pour l'extraction automatisée et structurée de données financières à partir de rapports PDF (locaux ou distants). 

Ce projet s'appuie sur Pydantic AI et les modèles Google Gemini pour analyser des documents financiers complexes et générer des rapports au format JSON standardisé, prêts à être intégrés dans des bases de données ou des pipelines d'analyse. 

## Fonctionnalités clés

- **Extraction Intelligente** : Convertit les PDF en Markdown (via pymupdf4llm) pour une compréhension contextuelle optimale par le LLM.

- **Validation Stricte (Pydantic)** : Garantit que les données extraites (dividendes, revenus par segments, nombre d'employés) respectent un schéma de données précis et des règles mathématiques strictes (ex: gestion des valeurs "en millions").

- **Architecture Clean Code** : Découplage total des responsabilités (téléchargement, traitement PDF, extraction IA, orchestration) facilitant la maintenance, l'évolution et l'ajout de nouveaux agents.

- **Gestion des sources multiples** : Accepte indifféremment des chemins de fichiers locaux ou des URL (avec téléchargement automatique et sécurisé).

- **Suite de Tests Intégrée** : Évaluations répétées ("Golden Dataset") via pytest pour mesurer et garantir la précision déterministe du modèle d'IA.

## Arborescence du Projet

L'application respecte le standard industriel "src-layout" :

```tree
histia-llm-agent/
├── data/
│   ├── downloads/        # Stockage des PDF téléchargés
│   └── output/           # Rapports financiers extraits (fichiers .json)
├── prompts/
│   └── system_prompt.txt # Instructions système pour le comportement du LLM
├── src/                  # Code source de l'application
│   ├── main.py           # Point d'entrée de l'application
│   ├── agent.py          # Orchestrateur principal (FinancialExtractor)
│   ├── document.py       # Traitement des PDF et requêtes HTTP
│   ├── models.py         # Schémas de données et de validation Pydantic
│   ├── config.py         # Gestion de la configuration et de l'environnement
│   └── utils.py          # Fonctions utilitaires partagées
├── tests/                # Suite de tests automatisés
│   ├── test_config.py
│   ├── test_document.py
│   └── test_extraction.py
├── pytest.ini            # Configuration des tests
└── README.md             # Documentation du projet
```

## Installation et Prérequis

### 1. Prérequis

- Python 3.10 ou supérieur

- Une clé API Google Gemini valide

### 2. Installation

Clonez le dépôt et configurez un environnement virtuel isolé :
```bash
## Installer les dépendances requises
pip install -r requirements.txt
```

### 3. Configuration de l'environnement

L'agent nécessite une clé API pour interagir avec les modèles Google. Définissez votre clé dans les variables de votre environnement système :

```bash
# Sur environnements Unix (Linux/macOS)
export GEMINI_API_KEY="votre_cle_api_ici"

# Sur environnements Windows (PowerShell)
$env:GEMINI_API_KEY="votre_cle_api_ici"
```

## Utilisation

Pour lancer le processus d'extraction sur le document cible (configuré par défaut dans le script principal):

```bash
python -m src.main
```

### Flux d'exécution :

1. Le système identifie la source (ex: Alphabet Q4 2024 Earnings Release).

2. Le fichier est téléchargé dans data/downloads/.

3. Le document PDF est converti en format Markdown.

4. L'agent IA analyse le contenu et structure les données requises.

5. Un fichier JSON sérialisé est généré dans data/output/ (ex: 2024q4-alphabet-earnings-release_extracted.json).

## Tests Unitaires et Validation 

Le projet inclut une suite de tests rigoureux utilisant pytest. Le test d'extraction s'exécute sur plusieurs itérations afin de s'assurer que le LLM produit des résultats constants et déterministes, minimisant ainsi le risque d'hallucinations.

Pour lancer l'intégralité de la suite de tests :

```bash
python -m pytest
```

## Stack Technique

- Langage : Python

- IA & Orchestration : Pydantic AI, Google GenAI (gemini-3.1-flash-lite)

- Validation de données : Pydantic

- Traitement Documentaire : PyMuPDF4LLM

- Tests: Pytest