import os
import sys
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

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "mysql":
        print("\n❌ Invalid command. Usage:\n"
            "  To create a database: python3 robot.py mysql create <database_name>\n"
            "  To list databases: python3 robot.py mysql list")
        sys.exit(1)

    _, command, action, *args = sys.argv

    if action == "create" and len(args) == 1:
        create_mysql_database(args[0])
    elif action == "list" and not args:
        list_mysql_databases()
    else:
        print("\n❌ Invalid command or action.")
        logger.warning("❌ Invalid command or action.")
