import pandas as pd
from sales_data_pipeline.src.utils.logging_setup import setup_logging

logger = setup_logging()

def transform_db_data(data):
    try:
        logger.info("Transforming database data...")
        order_df = pd.DataFrame(data)
        logger.info("Database data transformed successfully.")
        return order_df
    except Exception as e:
        logger.error(f"Error transforming database data: {e}")
        raise
