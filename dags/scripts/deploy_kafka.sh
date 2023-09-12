#!/bin/bash

# sudo docker run --name mono-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql
git clone https://github.com/amitsatpute-pyjs/kafka-connect.git /home/gsluser/app/kafka-connect/
cd /home/gsluser/app/kafka-connect/
./psql_setup.sh
