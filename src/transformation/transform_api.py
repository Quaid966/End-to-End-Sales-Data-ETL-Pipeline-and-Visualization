import pandas as pd
from sales_data_pipeline.src.utils.logging_setup import setup_logging

logger = setup_logging()

def transform_api_data(data):
    try:
        logger.info("Transforming API data...")
        df = pd.DataFrame(data)
        df = df[['id', 'price', 'category', 'rating']]
        df[['rate', 'count']] = pd.json_normalize(df['rating'])
        df = df.drop(columns=['rating'])
        transform_df = df.rename(columns={"id": "product_id"})
        logger.info("API data transformed successfully.")
        return transform_df
    except Exception as e:
        logger.error(f"Error transforming API data: {e}")
        raise

