from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker

class Engine(object):

    url = 'custom_connection_url'

engine = Engine()
