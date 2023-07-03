
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
