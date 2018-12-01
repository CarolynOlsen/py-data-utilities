import pandas as pd
import os
from dotenv import load_dotenv

# get database login information from environment file
load_dotenv('[PATH]/.env')
SERVER = os.environ.get('my_postgresql_server')
USER = os.environ.get('my_postgresql_user')
PASSWORD = os.environ.get('my_postgresql_pw')
DATABASE = os.environ.get('my_postgresql_db')

# create database connection
cxn = psycopg2.connect(host=SERVER, database=DATABASE, user=USER, password=PASSWORD)

# define SQL query
q = """
SELECT * 
FROM SALES
LIMIT 100
"""

# pull data in with pandas
df = pd.read_sql(q, cxn)
