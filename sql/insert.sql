COPY customers FROM '/docker-entrypoint-initdb.d/customers.csv' DELIMITER ',' NULL AS '' CSV HEADER;

--DELETE * FROM customers WHERE customer_id = "";
--DROP DUPLICATES * FROM customers WHERE customer_id == "";
--alter table users add primary key (customer_id);

COPY items FROM '/docker-entrypoint-initdb.d/items.csv' DELIMITER ',' NULL AS '' CSV HEADER;
COPY orders FROM '/docker-entrypoint-initdb.d/orders.csv' DELIMITER ',' NULL AS '' CSV HEADER;
COPY products FROM '/docker-entrypoint-initdb.d/products.csv' DELIMITER ',' NULL AS '' CSV HEADER;
