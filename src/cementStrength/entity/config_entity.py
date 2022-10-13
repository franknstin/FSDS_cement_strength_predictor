from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir",
    "ingested_data_train_dir",
    "ingested_data_test_dir"
    ])

DataValidationConfig = namedtuple("DataValidationConfig", [
    "data_validation_dir",
    "schema_file_path",
    "report_file_path",
    "report_page_file_path"
    ])