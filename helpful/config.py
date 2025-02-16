import os
from dotenv import load_dotenv

class __Settings:
    def __init__(self):
        load_dotenv()
        self.bot_token: str = os.getenv('TOKEN')

config = __Settings()
