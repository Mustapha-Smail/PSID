# Backend

- se mettre dans le dossier

```{shell}
cd backend
```

- installer les librairies

```{shell}
pip install django djangorestframework matplotlib plotly python-dotenv pandas graphviz numpy 
```

- aller dans le fichier .env **backend/.env** et modifier le path de ton fichier csv

```{env}
CSV_FILE=PATH/TO/CSV/FILE
```

- demarrer l'application

```{shell}
python manage.py runserver
```

### Nettoyage de données

- modifier le fichier **backend/backend_app/data/load_data.py**

### Dataviz

- créer des dataviz dans **backend/backend_app/views.py**

# Frontend

- se mettre dans le dossier

```{shell}
cd frontend
```

- installer les modules

```{shell}
npm install
```

- demarrer l'application

```{shell}
npm start
```
