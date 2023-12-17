import os
import logging
import logging.config
import mysql.connector
from dotenv import load_dotenv

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
load_dotenv(override=True)

def list_mysql_databases():
    try:
        connection = mysql.connector.connect(
            user=os.getenv('DB_USER', 'robot'),
            password=os.getenv('DB_PASSWORD', ''),
            host=os.getenv('DB_HOST', 'localhost')
        )
        cursor = connection.cursor()

        show_databases_query = "SHOW DATABASES"
        cursor.execute(show_databases_query)
        databases = [row[0] for row in cursor.fetchall()]

        print("\n📊 Available databases:\n")
        for db in databases:
            print(f" 📀 {db}")
        print("\n")

        logger.info(f"📊 Available databases: {', '.join(databases)}")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        logger.error(f"❌ Error: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
