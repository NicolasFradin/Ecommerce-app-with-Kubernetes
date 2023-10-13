COPY customers FROM '/docker-entrypoint-initdb.d/customers.csv' DELIMITER ',' NULL AS '' CSV HEADER;

ALTER TABLE customers
    ADD  created_at DATE DEFAULT current_date,
    ADD  updated_at DATE;                                   --not set default to keep first created row as null

COPY items FROM '/docker-entrypoint-initdb.d/items.csv' DELIMITER ',' NULL AS '' CSV HEADER;

ALTER TABLE items
    ADD  created_at DATE DEFAULT current_date,
    ADD  updated_at DATE;

COPY orders FROM '/docker-entrypoint-initdb.d/orders.csv' DELIMITER ',' NULL AS '' CSV HEADER;

ALTER TABLE orders
    ADD  created_at DATE DEFAULT current_date,
    ADD  updated_at DATE;

COPY products FROM '/docker-entrypoint-initdb.d/products.csv' DELIMITER ',' NULL AS '' CSV HEADER;

ALTER TABLE products
    ADD  created_at DATE DEFAULT current_date,
    ADD  updated_at DATE;
