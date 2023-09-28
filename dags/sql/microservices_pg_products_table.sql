-- public.products definition

-- Drop table

-- DROP TABLE public.products;

CREATE TABLE IF NOT EXISTS public.products (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	"name" varchar(255) NOT NULL,
	description varchar(255) NULL,
	picture varchar(255) NULL,
	"cost" float4 NULL DEFAULT '0'::real,
	categories varchar(255) NULL,
	created_at timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT products_pkey PRIMARY KEY (id)
);