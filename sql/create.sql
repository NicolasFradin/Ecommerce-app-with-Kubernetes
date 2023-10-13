DROP TABLE if exists Customers;
CREATE TABLE Customers (
    customer_id UUID NOT NULL,   --duplicated
    customer_unique_id UUID,
    customer_zip_code_prefix  VARCHAR(10),
    customer_city   VARCHAR(50),
    customer_state  VARCHAR(5),
    --created_at DATE,                          --not contained in the csv, so directly created in the insert.sql file.
    --updated_at DATE,
    PRIMARY KEY (customer_id)                   --not incremental because uuid and not int
);

DROP TABLE if exists Items;
CREATE TABLE Items (
    order_id UUID,
    order_item_id INTEGER NOT NULL,   --duplicated
    product_id  UUID,
    seller_id   UUID,
    shipping_limit_date  DATE,
    price FLOAT,
    freight_value FLOAT
    --PRIMARY KEY (order_item_id)
);

DROP TABLE if exists Orders;
CREATE TABLE Orders (
    order_id UUID NOT NULL,
    customer_id UUID,
    order_status  VARCHAR(50),
    order_purchase_timestamp   DATE,         -- date/time field value out of range: "0000-10-19 15:35:35"
    order_approved_at  DATE,                 -- date/time field value out of range: "0000-10-19 15:35:35"
    order_delivered_carrier_date DATE,
    order_delivered_customer_date DATE,
    order_estimated_delivery_date DATE
    --PRIMARY KEY (order_id)
);

DROP TABLE if exists Products;
CREATE TABLE Products (
    product_id VARCHAR(50) NOT NULL,
    product_category_name VARCHAR(50),
    product_name_lenght  VARCHAR(50),
    product_description_lenght   FLOAT,
    product_photos_qty  FLOAT,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT,
    product_category_name_english VARCHAR(50)
    --PRIMARY KEY (product_id)
);

