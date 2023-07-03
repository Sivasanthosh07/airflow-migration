



-- CREATE TABLE IF NOT EXISTS unsplash (
--     id VARCHAR(20) PRIMARY KEY,
--     username VARCHAR(20),
--     name VARCHAR(15),
--     portfolio_url VARCHAR(30),
--     image_url VARCHAR(200),
--     total_likes INT,
--     total_photos INT
-- );


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


DROP TABLE IF EXISTS Products;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE products (
  id char(36) NOT NULL ,
  name varchar(255) NOT NULL,
  description varchar(255) DEFAULT NULL,
  picture varchar(255) DEFAULT NULL,
  cost float(25) DEFAULT '0.00',
  categories json DEFAULT NULL,
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


