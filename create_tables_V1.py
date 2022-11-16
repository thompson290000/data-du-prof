from sqlalchemy import create_engine, MetaData, \
    Column, Integer, Numeric, String, Date, Table, ForeignKey
import configparser
from connect import engine

engine = engine
metadata = MetaData()
metadata.reflect(bind=engine)


# DDL for customers, products, stores, and transactions
customers_table = Table(
    "Evenement",
    metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("first_name", String(35), nullable=False),
    Column("last_name", String(35), nullable=False),
    Column("email", String(35), nullable=False),
    Column("address", String(135), nullable=False),
    Column("dob", Date, nullable=False)
)

products_table = Table(
    "products",
    metadata,
    Column("product_id", Integer, primary_key=True),
    Column("name", String(35), nullable=False),
    Column("price", Numeric(10,2), nullable=False)
)

stores_table = Table(
    "stores",
    metadata,
    Column("store_id", Integer, primary_key=True),
    Column("address", String(135), nullable=True)
)

transactions_table = Table(
    "transactions",
    metadata,
    Column("transactions_id", Integer, primary_key=True),
    Column("transaction_date", Date, nullable=False),
    Column("customer_id", ForeignKey("customers.customer_id"), nullable=False),
    Column("product_id", ForeignKey("products.product_id"), nullable=False),
    Column("store_id", ForeignKey("stores.store_id"), nullable=False)
)

# Start transaction to commit DDL to postgres database
with engine.begin() as conn:
    metadata.create_all(conn)

    for table in metadata.tables.keys():
        print(f"{table} successfully created")
