import psycopg2
import config

connection = psycopg2.connect(database=config.database_connection["DATABASE_NAME"],
                              user=config.database_connection["USER"],
                              password=config.database_connection["PASSWORD"],
                              host=config.database_connection["ENDPOINT"],
                              port=config.database_connection["PORT"])


