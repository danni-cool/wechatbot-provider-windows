# encoding:utf-8
import os
from common.log import logger

def get_root():
    return os.path.dirname(os.path.abspath(__file__))

def get_appdata_dir():
    data_path = os.path.join(get_root(), "")
    if not os.path.exists(data_path):
        logger.info("[INIT] data path not exists, create it: {}".format(data_path))
        os.makedirs(data_path)
    return data_path
