SELECT 'CREATE DATABASE microservices_orders'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'microservices_orders')\gexec

SELECT 'CREATE DATABASE microservices_products'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'microservices_products')\gexec