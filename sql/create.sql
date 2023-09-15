DROP TABLE if exists Customers;
CREATE TABLE Customers (
    customer_id VARCHAR(50) NOT NULL,
    customer_unique_id VARCHAR(50) NOT NULL,
    customer_zip_code_prefix  VARCHAR(10),
    customer_city   VARCHAR(20),
    customer_state  VARCHAR(5),
    PRIMARY KEY (customer_id)
);

DROP TABLE if exists Items;
CREATE TABLE Items (
    order_id VARCHAR(50) NOT NULL,
    order_item_id VARCHAR(50) NOT NULL,
    product_id  VARCHAR(50) NOT NULL,
    seller_id   VARCHAR(50) NOT NULL,
    shipping_limit_date  DATE NOT NULL,
    price FLOAT,
    freight_value FLOAT,
    PRIMARY KEY (order_item_id)
);

DROP TABLE if exists Orders;
CREATE TABLE Orders (
    order_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50) NOT NULL,
    order_status  VARCHAR(20) NOT NULL,
    order_purchase_timestamp   DATE NOT NULL,
    order_approved_at  DATE,
    order_delivered_carrier_date DATE,
    PRIMARY KEY (order_id)
);

DROP TABLE if exists Products;
CREATE TABLE Products (
    product_id VARCHAR(50) NOT NULL,
    product_category_name VARCHAR(20),
    product_name_lenght  VARCHAR(20),
    product_description_lenght   FLOAT,
    product_photos_qty  FLOAT,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT,
    product_category_name_english FLOAT,
    PRIMARY KEY (product_id)
);

