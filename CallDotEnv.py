'''
USAGE: Store your API keys, passwords, etc. locally in a file named ".env"

.env file should be in a format with a new line per item you want to save, e.g.:
EXAMPLE_API_KEY = 'suschweg1244151ljysdfa'
'''


import os
from dotenv import load_dotenv

load_dotenv("PATH/.env")
EXAMPLE_API = os.getenv('EXAMPLE_API_KEY')
