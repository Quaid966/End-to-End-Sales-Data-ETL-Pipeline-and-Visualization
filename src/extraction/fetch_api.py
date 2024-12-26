
import requests
from sales_data_pipeline.src.utils.logging_setup import setup_logging

logger = setup_logging()

def fetch_api_data(api_url):
    try:
        logger.info("Fetching data from API...")
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info("API data fetched successfully.")
        return data
    except requests.RequestException as e:
        logger.error(f"Error fetching data from API: {e}")
        raise