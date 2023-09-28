-- public.orders definition

-- Drop table

-- DROP TABLE public.orders;

CREATE TABLE IF NOT EXISTS public.orders (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	product_ids json NULL,
	user_id uuid NOT NULL,
	total_cost float4 NULL DEFAULT '0'::real,
	created_at timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at timestamptz NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT orders_pkey PRIMARY KEY (id)
);


-- public.orders foreign keys

ALTER TABLE public.orders ADD CONSTRAINT orders_user_id_foreign FOREIGN KEY (user_id) REFERENCES public.users(id);