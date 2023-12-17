import os
import sys
import logging
import logging.config
import mysql.connector
from dotenv import load_dotenv
from src.mysql.create_database import create_mysql_database
from src.mysql.list_databases import list_mysql_databases

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
load_dotenv(override=True)

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