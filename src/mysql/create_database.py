import os
import logging
import logging.config
import mysql.connector
from dotenv import load_dotenv

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
load_dotenv(override=True)

def create_mysql_database(database_name):
    try:
        connection = mysql.connector.connect(
            user=os.getenv('DB_USER', 'robot'),
            password=os.getenv('DB_PASSWORD', ''),
            host=os.getenv('DB_HOST', 'localhost')
        )
        cursor = connection.cursor()
        create_db_query = f"CREATE DATABASE {database_name}"
        cursor.execute(create_db_query)
        connection.commit()

        print(f"\n✅ Database '{database_name}' created successfully.\n")
        logger.info(f"✅ Database '{database_name}' created successfully.")

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
            print(f"❌ Error: Database '{database_name}' already exists.")
            logger.warning(f"❌ Database '{database_name}' already exists.")
        else:
            print(f"❌ Error: {err}")
            logger.error(f"❌ Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
