#!/bin/bash

echo "creating the database: crpto"
#run the setup script to create the DB and the schema in the DB
/opt/mssql-tools/bin/sqlcmd -S db -U ${DB_USER} -P ${DB_PASSWORD} -d master -i ./app/init_db/create_db.sql