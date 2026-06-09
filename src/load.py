import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    os.getenv('DATABASE_URL')
)

def load(result):
    result.to_sql(
        name = 'vaccination_coverage',
        con = engine,
        if_exists = 'append',
        index = False
    )