from datetime import datetime, timedelta
from stockframe import StockData


def toUpdate(hourVal, minuteVal, secondsVal):
    """Update on Weekdays only"""
    day = datetime.now().weekday()
    if day < 5:
        history = StockData("AAPL").getHistData(period="5d")
        prevdate = history.index[-1].date()  # Convers timestamp to datetime
        now = datetime.now().date()  # Today's date
        hour = datetime.now().hour
        minute = datetime.now().minute
        seconds = datetime.now().second

        if now != prevdate and hour == hourVal and minute == minuteVal and seconds == secondsVal:
            return True
        else:
            return False
