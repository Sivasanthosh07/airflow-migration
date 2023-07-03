DROP TABLE IF EXISTS users;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE users (
  id char(36) NOT NULL ,
  full_name varchar(255) NOT NULL,
  address varchar(255) DEFAULT NULL,
  email varchar(255) DEFAULT NULL,
  created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);



DROP TABLE IF EXISTS orders;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE orders (
  id char(36) NOT NULL ,
  product_ids json DEFAULT NULL,
  user_id char(36) NOT NULL,
  total_cost float(25) DEFAULT '0.00',
  created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
)


-- INSERT INTO orders VALUES ('297eb24e-1c92-4852-8350-ca407dfd0eef',NU,'2c5be9a7-2b81-44d0-bdf2-3f79f8dbea3e',65.50,'2023-03-17 06:39:11','2023-03-17 06:39:11'),('a022936b-9c35-46f3-85c4-e96f9de1f544','[\"d353c4ed-3255-4550-860a-147580c27e89\"]','2c5be9a7-2b81-44d0-bdf2-3f79f8dbea3e',124.00,'2023-03-17 06:39:11','2023-03-17 06:39:11'),('e0ff295b-5d84-4a0a-b7db-608ed0865dcd','[\"bcb2fa74-90be-487e-8dc0-c6bfd379c633\", \"1d7402b6-522b-42ad-84bc-e58d7402e3fb\"]','2c5be9a7-2b81-44d0-bdf2-3f79f8dbea3e',80.48,'2023-03-17 06:39:11','2023-03-17 06:39:11'),('ee7c8762-41c8-4570-93f5-339503dced5b','[\"8ab7a322-9ad7-4f4e-8230-046e214bdc49\"]','2c5be9a7-2b81-44d0-bdf2-3f79f8dbea3e',36.45,'2023-03-17 06:39:11','2023-03-17 06:39:11');
