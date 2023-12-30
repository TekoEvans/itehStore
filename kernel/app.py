from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json, hashlib

# Création de l'objet application

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Valeurs du fichier de paramètres de la société
try :
    with open('society_config.json') as config :
        data = json.load(config)
except Exception:
    with open('../society_config.json') as config :
        data = json.load(config)

# Configurations de la connection à la base de données

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de la base de données

db = SQLAlchemy(app)

# Définition de la clé secrètre de l'application pour l'utilisation de session

app.secret_key = "90d5cddde08c47b07b78f997e5105447cdf8d3aa18fd90de7e5175f1cc90060f" 

# Fonction de modification des valeurs du fichier de paramètres de la société

def updateConfigFile(data):
    with open('society_config.json', 'w') as file :
        json.dump(data, file)

def createHash(value):
    return hashlib.sha256(value.encode()).hexdigest()