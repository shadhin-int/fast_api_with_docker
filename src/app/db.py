import os

from databases import Database
from sqlalchemy import create_engine, MetaData

Database_URL = os.getenv('DATABASE_URL')
# SQLAlchemy
engine = create_engine(Database_URL)
metadata = MetaData()

# database query builder

database = Database(Database_URL)