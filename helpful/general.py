from datetime import datetime, timedelta
from typing import Optional, Union, Any
from pytz import timezone


def log(text: Any) -> None:
    print(f'[{time_now("%Y-%m-%d %H:%M:%S")}] [INFO]: {text}', flush=True)

def time_now(strftime: str = None, location: str = 'Europe/Moscow') -> Union[datetime, str]:
    date = datetime.now(timezone(location))
    if strftime is None:
        return date
    return date.strftime(strftime)
