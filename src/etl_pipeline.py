import pandas as pd

from sales_data_pipeline.src.extraction.fetch_api import fetch_api_data
from sales_data_pipeline.src.extraction.fetch_db import fetch_db_data
from sales_data_pipeline.src.transformation.transform_api import transform_api_data
from sales_data_pipeline.src.transformation.transform_db import transform_db_data
from sales_data_pipeline.src.transformation.merge_data import merge_data
from sales_data_pipeline.src.loading.load_to_db import load_data_to_db
from sales_data_pipeline.src.utils.config import API_URL

def etl_pipeline():
    try:
        # Extract
        api_data = fetch_api_data(API_URL)
        query = "SELECT * FROM orders;"
        db_data = fetch_db_data(query)

        # Transform
        product_df = transform_api_data(api_data)
        order_df = transform_db_data(db_data)

        # Merge
        final_data = merge_data(order_df, product_df)
        df = pd.DataFrame(final_data)
        print(df.info())
        # Validation
        if final_data.empty:
            logger.warning("Final merged data is empty.")
        else:
            logger.info(f"Pipeline completed successfully with {len(final_data)} rows.")

            # Load
            load_data_to_db(final_data, table_name="pro_order")

        return final_data
    except Exception as e:
        logger.critical(f"ETL pipeline failed: {e}")
        raise

if __name__ == "__main__":
    from sales_data_pipeline.src.utils.logging_setup import setup_logging
    logger = setup_logging()
    logger.info("Starting ETL pipeline...")
    data = etl_pipeline()
    logger.info("ETL pipeline finished.")
    print(data.head())
