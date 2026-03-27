from urllib.parse import quote_plus

class Config:
    SECRET_KEY = "super_secret_key"

    _pwd = quote_plus("Ust@1411*****")  # ← solo encodea la contraseña
    
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://ludwig:{_pwd}@suumph.database.windows.net:1433/NoLine"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
        "&Connection+Timeout=30"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False