import os
import urllib.request as request
from zipfile import ZipFile
from cementStrength.entity import DataIngestionConfig
from cementStrength import logger
from cementStrength.utils import get_size
from tqdm import tqdm
from pathlib import Path





class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("downloading data file")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename = self.config.local_data_file
            )
        logger.info("file downloaded")