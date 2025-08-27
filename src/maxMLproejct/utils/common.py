import os
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
import joblib
import json
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
from log_setup import log_setup
import logging.config
log_setup('logging.yaml')
logger = logging.getLogger(__name__)

@ensure_annotations
def read_yaml(config_path:str = Path) -> Any:
    '''Reads yaml files and returns a value of NoneType'''
    try:
        with open(config_path,'r') as file: 
            config = yaml.safe_load(file) #reads the yaml file into the python environment as a dict
        return config
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(directories_path: list) -> Any:
    '''Creates directories'''
    try:
        for path in directories_path:
            os.makedirs(path,exist_ok=True)
            logger.info(f'Created directory at: {path}')
    except Exception as e:
        raise e
    logger.error(f'Could not create directories')

@ensure_annotations
def save_json(path: Path,data: dict):
    '''Saves json data'''
    try:
        with open(path,'w') as file:
            json.dump(data,file,indent=4)
        logger.info(f'Json file saved at {path}')
    except Exception as e:
        raise e
    logger.error(f'Could not write json data to {path}')

@ensure_annotations
def load_json(path: Path):
    '''Loads json file data'''
    try:
        with open(path,'r') as file:
            json.loads(file)
        logger.info(f'Json file successfully loaded from {path}')
    except Exception as e:
        raise e
    logger.error(f'Unable to load json file')

@ensure_annotations
def save_bins(path: Path,data):
    '''Saves binary data'''
    try:
        with open(path,'w') as file:
            joblib.dump(value=data,filename=path)
        logger.info(f'binary data file saved at {path}')
    except Exception as e:
        raise e
    logger.error(f'Unable to save binary data to {path}')    

@ensure_annotations
def load_bins(path: Path) -> Any:
    '''Loads binary data'''
    try:
        with open(path,'r') as file:
            json.loads(file)
        logger.info(f'Binary data file successfully loaded from {path}')
    except Exception as e:
        raise e
    logger.error(f'Unable to load binary data file')

@ensure_annotations
def get_file_size(path: Path) -> str:
    '''Gets file size in kb'''
    try:
        size_in_kb = round(os.path.getsize(path)/1024,2)
        return f'- {size_in_kb} KB'
    except FileNotFoundError:
        raise FileNotFoundError(f'{path} not found')