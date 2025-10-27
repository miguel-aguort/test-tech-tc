# Import
import logging
import os
from dotenv import load_dotenv
import pandas as pd

from utils.database import multimodal_ocr, init_db, load_data

# 0- config
load_dotenv()

LOG_LEVEL = os.getenv('LOG_LEVEL')
level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
_log = logging.getLogger(__name__)

# 1- Generar parquet if not exists
multimodal_ocr()

# 2- Cargar parquet e ingestar datos en sqlite vec
df = load_data()
pdf_content = df["contents"].astype(str).tolist()

vector_db = init_db()
vector_db.add_texts(pdf_content)


# 3-  