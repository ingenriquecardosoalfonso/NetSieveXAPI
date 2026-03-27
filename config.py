import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super_secret_key')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or (
        "mssql+pyodbc://ludwig:{}@suumph.database.windows.net:1433/NoLine"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
        "&Connection+Timeout=30"
    ).format(quote_plus("Ust@1411*****"))

    SQLALCHEMY_TRACK_MODIFICATIONS = False