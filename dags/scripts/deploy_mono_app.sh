#!/bin/bash

# sudo docker run --name mono-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql
git clone https://github.com/amitsatpute-pyjs/kafka-connect.git ~/app/
cd ~/app/kafka-connect/
docker-compose up postgres
git clone https://github.com/amitsatpute-pyjs/monolith-to-microservices.git ~/app/
cd ~/app/monolith-to-microservices/monolith
cp .env.example .env
sed -i 's/<username>/root/g' .env
sed -i 's/<password>/password/g' .env
npm ci
sudo npm install pm2 -g
pm2 --name monoApp start npm -- start
# npm start
cd ../react-app
npm ci
pm2 --name monoUI start npm -- start
# npm start

