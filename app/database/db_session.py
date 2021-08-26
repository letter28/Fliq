from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

from constants import DB_USER, DB_PSWRD, DB_HOST, DB_NAME, DB_PORT, DB_SCHEMA


conn_string = f"postgresql+psycopg2://{DB_USER}:{DB_PSWRD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(conn_string)

db_session = scoped_session(sessionmaker(bind=engine))

metadata = MetaData(schema=DB_SCHEMA)

Base = declarative_base(metadata=metadata)

Base.query = db_session.query_property()