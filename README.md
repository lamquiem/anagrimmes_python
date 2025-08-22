# Anagrimes Python

## 1. Prérequis

- Python 3.9+  
- pip  
- (Optionnel) Git  
- (Optionnel) Virtualenv/venv

## 2. Décompression de l’archive

```bash
unzip anagrimes_package.zip -d anagrimes_python
cd anagrimes_python
```

## 3. Environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou .\venv\Scripts\Activate.ps1 sous Windows
```

## 4. Installation des dépendances

```bash
pip install --upgrade pip
pip install -r api/requirements.txt
```

## 5. Initialisation de la base de données

```bash
python init_db.py
```

## 6. Utilisation des scripts

- `scripts/articles_list.py dump.xml.bz2 articles.txt`  
- `scripts/wikt_dump_diff.py ancien.xml.bz2 nouveau.xml.bz2 diff.txt`  
- `scripts/create_xml_dico.py dump.xml.bz2 dico.xml`  
- `scripts/extract_tables.py dump.xml.bz2 tables_output/`  
- `scripts/list_vs_dump.py liste.txt articles.txt missing.txt`

## 7. Lancement de l’API

```bash
cd api
uvicorn main:app --reload
# Ouvrir http://127.0.0.1:8000/
```

## 8. Structure du projet

```
anagrimes_python/
├── api/
├── scripts/
├── init_db.py
└── anagrimes.db (après init)
```