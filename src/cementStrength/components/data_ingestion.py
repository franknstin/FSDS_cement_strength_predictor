import os
import urllib.request as request
from zipfile import ZipFile
from cementStrength.entity import DataIngestionConfig
from cementStrength import logger
from cementStrength.utils import get_size
from tqdm import tqdm
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

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

    # def unzip_file(self):
    #     logger.info("extracting zip file")
    #     with ZipFile(file=self.config.local_data_file) as zf:
    #         zf.extractall(self.config.unzip_dir)
    #     logger.info("file extraction done")


    def split_data_as_train_test(self):
        downloaded_file_path = self.config.local_data_file
        train_filename = "train.csv"
        test_filename = "test.csv"
        train_file_path = os.path.join(self.config.ingested_data_train_dir, train_filename)
        test_file_path = os.path.join(self.config.ingested_data_test_dir, test_filename)

        logger.info("reading excel file into pandas dataframe")
        cement_strength_df = pd.read_excel(downloaded_file_path)
        X = cement_strength_df.iloc[:,:-1]
        y = cement_strength_df.iloc[:,-1]
        logger.info("splitting df in train and test")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        if X_train is not None:
            logger.info("saving X_train....")
            X_train.to_csv(train_file_path, index=False)
            logger.info("saved X_train")

        if X_test is not None:
            logger.info("saving X_test....")
            X_test.to_csv(test_file_path, index=False)
            logger.info("saved X_test")

    def initiate_data_ingestion(self):
        pass