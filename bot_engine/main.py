#!/usr/bin/env python3

import telebot
from optparse import OptionParser

path = {
    'api': 'bot_engine/access/api.txt',
    'chat_id': 'bot_engine/access/chat_id.txt',
    'info_folder': 'bot_engine/info/'
}


def message():
    if options.company == '':
        msg = f'<b>Внимание, новая заявка!</b>\n\n' \
              f'<b>Имя:</b> <i>{options.name}</i>\n' \
              f'<b>Номер телефона:</b> <i>{options.phone}</i>\n' \
              f'<b>Компания:</b> <i>Пользователь не имеет компании</i>\n' \
              f'<b>Сообщение:</b> <i>{options.message}</i>'
    else:
        msg = f'<b>Внимание, новая заявка!</b>\n\n' \
              f'<b>Имя:</b> <i>{options.name}</i>\n' \
              f'<b>Номер телефона:</b> <i>{options.phone}</i>\n' \
              f'<b>Компания пользователя:</b> <i>{options.company}</i>\n' \
              f'<b>Сообщение:</b> <i>{options.message}</i>'
    return msg


parser = OptionParser()
parser.add_option('-n', '--name', dest='name',
                  help='Name of user', metavar='NAME')
parser.add_option('-p', '--phone', dest='phone',
                  help='Phone Number', metavar='PHONE')
parser.add_option('-c', '--company', dest='company',
                  help='Company', metavar='COMPANY')
parser.add_option('-m', '--message', dest='message',
                  help='Message', metavar='MESSAGE')

(options, args) = parser.parse_args()

with open(path['api'], 'r') as apifile:
    bot = telebot.TeleBot(apifile.read())

with open(path['chat_id'], 'r') as chat_id:
    bot.send_message(chat_id=chat_id.read(), text=message(), parse_mode='html')
