import psycopg2
from sales_data_pipeline.src.utils.logging_setup import setup_logging
from sales_data_pipeline.src.utils.config import DB_CONFIG_desitination

logger = setup_logging()

def load_data_to_db(dataframe, table_name):
    """
    Load a Pandas DataFrame into the specified database table.
    """
    global conn
    try:
        logger.info(f"Loading data into the '{table_name}' table...")
        conn = psycopg2.connect(**DB_CONFIG_desitination )
        cursor = conn.cursor()

        # Create insert query dynamically based on DataFrame columns
        columns = ', '.join(dataframe.columns)
        placeholders = ', '.join(['%s'] * len(dataframe.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Execute insert query row by row
        for _, row in dataframe.iterrows():
            cursor.execute(insert_query, tuple(row))

        conn.commit()
        logger.info(f"Data successfully loaded into the '{table_name}' table.")
    except psycopg2.Error as e:
        logger.error(f"Error loading data into the database: {e}")
        raise
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            logger.info("Database connection closed.")
