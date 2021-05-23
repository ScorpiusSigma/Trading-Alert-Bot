import telegram
import requests


SICTOKEN = '1269694800:AAGBDBPjTqnelY3WNkvqp6SZurjYrCMe-vc'
SICAlertChatID = '-1001371960899'


def SICAlert_bot(text):
    """ Sends messages to SIC Alerts channel """
    # Bot info
    bot = telegram.Bot(token=SICTOKEN)
    # print(bot.get_me())

    # sends messages to chat
    # Chat_id - https://web.telegram.org/#/im?p=c"1371960899"_2218953917755105830
    bot.send_message(chat_id=SICAlertChatID, text=text)


# def sgx(data):

#     EXCHANGE = data['Exchange']
#     DATETIME = data['DateTime']
#     ISSUERNAME = data['Issuer Name']
#     SECURITYNAME = data['Security Name']
#     TITLE = data['Title']
#     CATEGORY = data['Category']
#     LINK = data['link']

#     messageFormat = 'Exchange: {0}\n\nDateTime: {1}\nIssuer Name: {2}\nSecurity Name: {3}\nTitle:{4}\nCategory:{5}\nLink:{6}\n'.format(
#         EXCHANGE, DATETIME, ISSUERNAME, SECURITYNAME, TITLE, CATEGORY, LINK)
#     return messageFormat
