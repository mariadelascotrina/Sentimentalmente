import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()

password = os.getenv("pass_sql")
#dbName = "api"
#connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
#engine = alch.create_engine(connectionData)

db_name = "api"
conec = f"mysql+pymysql://root:{password}@localhost/{db_name}"
engine = alch.create_engine(conec)