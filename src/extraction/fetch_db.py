
import psycopg2
from psycopg2.extras import RealDictCursor
from sales_data_pipeline.src.utils.logging_setup import setup_logging
from sales_data_pipeline.src.utils.config import DB_CONFIG

logger = setup_logging()

def fetch_db_data(query):
    try:
        logger.info("Connecting to the database...")
        conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        logger.info("Database data fetched successfully.")
        return data
    except psycopg2.Error as e:
        logger.error(f"Error fetching data from the database: {e}")
        raise
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            logger.info("Database connection closed.")