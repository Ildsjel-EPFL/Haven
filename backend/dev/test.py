import os
from dotenv import load_dotenv

load_dotenv()

RCP_api_key = os.getenv("RCP_API_KEY")
print(f"RCP_api_key: {RCP_api_key}")    # Does work, prints the value of RCP_API_KEY from .env file