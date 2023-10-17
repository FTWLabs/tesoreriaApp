from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database

usuario = 'localhost'
contraseña = 'Emilio.1952' 

engine = create_engine(
  "mysql+pymysql://root:"+contraseña+"@"+usuario+":3306/storedb"
)

if not database_exists(engine.url):
  create_database(engine.url)
# En la variable engine se usó
# el usuario y contraseña del
# MySQL local

meta = MetaData()

conn = engine.connect()