#!/bin/bash

pip install --user -r requirements.txt

if [ ! -d storage ]; then
    mkdir storage
    echo -e "\n✅ 'storage' directory created."
else
    echo -e "\n✅ 'storage' directory already exists."
fi

if [ ! -d storage/logs ]; then
    mkdir storage/logs
    echo -e "✅ 'storage/logs' directory created."
else
    echo -e "✅ 'storage/logs' directory already exists."
fi

if [ ! -f log.conf ]; then
    echo "[loggers]
keys=root

[handlers]
keys=fileHandler

[formatters]
keys=fileFormatter

[logger_root]
level=INFO
handlers=fileHandler

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=fileFormatter
args=('storage/logs/operations.log', 'w')

[formatter_fileFormatter]
    format=%(asctime)s - %(name)s - %(levelname)s - %(message)s" > log.conf
    echo -e "✅ 'log.conf' file created with default configuration."
else
    echo -e "✅ 'log.conf' file already exists."
fi

if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "✅ '.env' file copied from '.env.example'."
else
    echo -e "✅ '.env' file already exists."
fi

echo -e "\n🎉 Installation successful! Before running your script, configure the .env file with your MySQL credentials."
echo "🔑 After configuring .env, you can run: python3 robot.py mysql create test_database"
