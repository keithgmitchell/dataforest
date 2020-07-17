from pathlib import Path
from typing import Union

from dataforest.config.MetaConfig import MetaConfig
from dataforest.utils.loaders.load_config import load_config


def update_config(config: Union[dict, str, Path]):
    config = load_config(config)
    MetaConfig._CONFIG = config