"""Config file for project-wide variables and settings."""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT_DIR / "outputs"

## Environment Variables
OPENAI_KEY = os.getenv("OPENAI_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

class Config:
    """Configuration class for holding project settings."""
    def __init__(self):
        self.system_prompt: str = ("""You are an agent specialized in extracting structured data from invoice text.
                                   The text is extracted from PDF invoices.
                                   Your task is to extract the relevant fields.
                                   You output the extracted attributes in a structured format.
                                   
                                   Rules for extraction:
                                   - Only use information present in the text.
                                   - return null for missing values.
                                   - return "Not sure" for uncertain values."""
                                   )
    
def get_config() -> Config:
    """Function to get the configuration settings."""
    return Config()
    