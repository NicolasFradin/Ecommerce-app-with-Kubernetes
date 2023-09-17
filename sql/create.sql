DROP TABLE if exists Customers;
CREATE TABLE Customers (
    customer_id VARCHAR(50) NOT NULL,   --duplicated
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix  VARCHAR(10),
    customer_city   VARCHAR(50),
    customer_state  VARCHAR(5)
    --PRIMARY KEY (customer_id)
);

DROP TABLE if exists Items;
CREATE TABLE Items (
    order_id VARCHAR(50) ,
    order_item_id VARCHAR(50) NOT NULL,   --duplicated
    product_id  VARCHAR(50),
    seller_id   VARCHAR(50),
    shipping_limit_date  DATE,
    price FLOAT,
    freight_value FLOAT
    --PRIMARY KEY (order_item_id)
);

DROP TABLE if exists Orders;
CREATE TABLE Orders (
    order_id VARCHAR(50) NOT NULL,
    customer_id VARCHAR(50),
    order_status  VARCHAR(50),
    order_purchase_timestamp   VARCHAR(50),    -- date/time field value out of range: "0000-10-19 15:35:35"
    order_approved_at  VARCHAR(50), -- date/time field value out of range: "0000-10-19 15:35:35"
    order_delivered_carrier_date VARCHAR(50),
    order_delivered_customer_date VARCHAR(50),
    order_estimated_delivery_date VARCHAR(50)
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

