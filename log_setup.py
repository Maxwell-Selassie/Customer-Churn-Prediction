import logging.config
import os
from pathlib import Path
import yaml
from src.maxMLproejct.utils.common import read_yaml
from box.exceptions import BoxValueError

def log_setup(config_path: str = "logging.yaml") -> None:
    readYaml = read_yaml(config_path)  # now guaranteed to be a dict

    # Ensure directories exist for file handlers
    for handler in (readYaml.get("handlers") or {}).values():
        if not handler:
            raise ValueError("YAML handlers are empty")

        filename = handler.get("filename")
        if filename:
            Path(os.path.dirname(filename)).mkdir(parents=True, exist_ok=True)
        else:
            # Only file-based handlers have filenames; skip console handlers
            continue

    logging.config.dictConfig(readYaml)