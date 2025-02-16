import os
from dotenv import load_dotenv

load_dotenv()

bot_token: str = os.getenv('TOKEN')
bots = {
    'plansbot': 'РКСИ Планшетка',
    'rksibot': 'Журнал ИС',
    'testbot': 'YarTestBot',
}
