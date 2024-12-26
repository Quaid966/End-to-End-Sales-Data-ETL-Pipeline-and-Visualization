

import pandas as pd
from sales_data_pipeline.src.utils.logging_setup import setup_logging

logger = setup_logging()

def merge_data(order_df, product_df):
    try:
        logger.info("Merging data...")
        merged_df = pd.merge(order_df, product_df, on="product_id", how="inner")
        logger.info("Data merged successfully.")
        return merged_df
    except Exception as e:
        logger.error(f"Error merging data: {e}")
        raise