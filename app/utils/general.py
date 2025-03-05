import os
import config
from pytz import timezone
from typing import Union, Optional
from datetime import datetime, timedelta


def time_now(strftime: str = None, location: str = 'Europe/Moscow') -> Union[datetime, str]:
    date = datetime.now(timezone(location))
    if strftime is None:
        return date
    return date.strftime(strftime)
