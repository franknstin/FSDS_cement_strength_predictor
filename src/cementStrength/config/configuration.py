from collections import namedtuple
from cementStrength.constants import *
from cementStrength.utils import read_yaml, create_directories
import os
import urllib.request as request
from zipfile import ZipFile
from cementStrength import logger
from cementStrength.entity.config_entity import DataIngestionConfig, DataValidationConfig


class ConfigurationManager:
    def __init__(self, 
                config_filepath = CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        create_directories([config.ingested_data_train_dir, config.ingested_data_test_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
            ingested_data_train_dir = config.ingested_data_train_dir,
            ingested_data_test_dir= config.ingested_data_test_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_vaidation

        data_validation_dir = config.root_dir
        report_file_path = os.path.join(data_validation_dir, config.report_file_name)
        report_page_file_path = os.path.join(data_validation_dir, config.report_page_file_name)

        data_validation_config = DataValidationConfig(
            data_validation_dir = data_validation_dir,
            schema_file_path = config.schema_dir, 
            report_file_path =  report_file_path,
            report_page_file_path = report_page_file_path
        )
        return data_validation_config
