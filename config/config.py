from dotenv import load_dotenv
import os

# Carga las variables de entorno del archivo .env
load_dotenv()

apiVersion = os.getenv("API_VERSION")

def get_string_connection():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_schema = os.getenv("DB_SCHEMA")
    db_port = os.getenv("DB_PORT")
    return "mysql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_schema)
