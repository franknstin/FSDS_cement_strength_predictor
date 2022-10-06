from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir",
    "ingested_data_train_dir",
    "ingested_data_test_dir"
    ])