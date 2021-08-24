from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

from constants import USER, PASSWORD, HOST, DATABASE, PORT, SCHEMA


conn_string = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(conn_string)

db_session = scoped_session(sessionmaker(bind=engine))

metadata = MetaData(schema=SCHEMA)

Base = declarative_base(metadata=metadata)

Base.query = db_session.query_property()