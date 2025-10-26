# Import
import logging
import os
from dotenv import load_dotenv

from utils.database import multimodal_ocr

# 0- config
load_dotenv()

LOG_LEVEL = os.getenv('LOG_LEVEL')
level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
_log = logging.getLogger(__name__)

# 1- Generar parquet
_log
multimodal_ocr()

# 2- Cargar parquet e ingestar datos en sqlite vec

# 3-  