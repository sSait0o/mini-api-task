Commandes essentielles — mini-api-task

PowerShell (Windows)

```powershell
# cloner le dépôt (si nécessaire)
git clone <repo-url>
cd <repo-folder>

# créer et activer un venv
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# installer les dépendances
pip install -r requirements.txt

# (optionnel) générer requirements.txt actuel depuis le venv
pip freeze > requirements.txt

# lancer l'interface CLI
py main.py

# (optionnel) lancer une app Flask si 'app.py' existe
py app.py
# ou
$env:FLASK_APP = "app.py"
flask run
```

Bash (macOS / Linux)

```bash
# cloner le dépôt (si nécessaire)
git clone <repo-url>
cd <repo-folder>

# créer et activer un venv
python3 -m venv .venv
source .venv/bin/activate

# installer les dépendances
pip install -r requirements.txt

# (optionnel) générer requirements.txt actuel depuis le venv
pip freeze > requirements.txt

# lancer l'interface CLI
python main.py

# (optionnel) lancer une app Flask si 'app.py' existe
python app.py
# ou
export FLASK_APP=app.py
flask run
```
