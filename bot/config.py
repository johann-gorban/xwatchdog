from pathlib import Path
from dotenv import load_dotenv
from os import getenv

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

BOT_TOKEN_API=getenv('BOT_TOKEN_API')

MAX_CAPACITY=100

URL = "https://www.exponent.finance/liquidity/xsol-26Nov25"
PERIOD_SEC = 60