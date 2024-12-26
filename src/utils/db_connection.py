import psycopg2
from sales_data_pipeline.src.utils.config import DB_CONFIG

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)