import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from the .env file into the environment
load_dotenv()

# Fetch the key securely
# We use os.environ.get() so it doesn't crash if the key is missing, 
# or you can use os.environ["RCP_API_KEY"] to force an error if it's missing.
RCP_api_key = os.getenv("RCP_API_KEY")

if not RCP_api_key:
    raise ValueError("RCP_API_KEY is not set. Please check your .env file.")

# Initialize the OpenAI-compatible model
llm = ChatOpenAI(
    api_key=RCP_api_key,
    base_url="https://inference.rcp.epfl.ch/v1", 
    # base_url="https://inference-rcp.epfl.ch/v1", # Access from outside EPFL; limited endpoints and HTTP method filtering apply
    model="swiss-ai/Apertus-large", # Alias for the latest version of the Large model, avoid EOL problems with specific versions
    temperature=0.2,  # Lower temperature for more deterministic responses
)