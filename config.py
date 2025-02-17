import os
from dotenv import load_dotenv

load_dotenv()

bot_token: str = os.getenv('BOT_TOKEN')
sql_url: str = os.getenv('SQL_URL')
bots = {
    'plansbot': 'РКСИ Планшетка',
    'rksibot': 'Журнал ИС',
    'testbot': 'YarTestBot',
}
