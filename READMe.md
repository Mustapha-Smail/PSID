# Backend

- se mettre dans le dossier

```{shell}
cd backend
```

- installer les librairies

```{shell}
pip install mysqlclient django djangorestframework matplotlib plotly python-dotenv pandas graphviz numpy
```

- Si problème d'installations de mysqlclient verifiez la [documentation](https://pypi.org/project/mysqlclient/)

- aller dans le fichier .env **backend/.env** et modifier le path de ton fichier csv

```{env}
CSV_FILE=PATH/TO/CSV/FILE
```

- aller dans **backend/backend/settings.py** et mettre à jour les infos de la BD

```{python}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'psid',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Use your MySQL server's hostname or IP address
        'PORT': '3306',       # MySQL default port
    }
}
```

- lancer les migrations

```{shell}
python manage.py makemigrations
python manage.py migrate
```

- lancer les insertions

```{shell}
python manage.py insert_data
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
