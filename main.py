import requests
from finviz.screener import Screener
from bot import SICAlert_bot
from datetime import datetime
################################## Testing Ground ##################################


def testGround():
    print("entered testing ground")
    url = "https://fintel.io/ss/us/sndl"
    response = requests.get(url)
    print(response.text)

################################## Testing Ground ##################################


stock_list = []


def app():
    print("Scorpius Sigma\n")
    filters = ['sh_float_u100', 'sh_outstanding_u100', 'sh_short_o25', 'sh_price_u5']  # Shows companies in NASDAQ which are in the S&P500
    screener = Screener(filters=filters, table='Overview', order='ticker')  # Get the performance table and sort it by price ascending
    for stock in screener:
        company = stock['Company']
        price = stock['Price']
        data = "Company: {0}\nPrice: {1}\n".format(company, price)
        stock_list.append(data)


if __name__ == "__main__":
    # testGround()
    while(1):
        app()
        date = datetime.now().date()
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second

        if hour == 12 and minute == 00 and second == 00:

            try:
                text = "Date: {0}\n\n{1}".format(date, "\n".join(stock_list))
                print(text)
                SICAlert_bot(text)  # Sends message to telegram
                stock_list = []
                print("Text sent at {0}".format(datetime.now()))
            except Exception as e:
                print(e)
