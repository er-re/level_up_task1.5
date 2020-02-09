from sqlalchemy import create_engine


class Engine:
    __user = ""
    __pass = ""
    __sever = ""
    __port = ""
    __database = ""
    __connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(__user, __pass, __sever, __port, __database)
    engine = create_engine(__connection_string)