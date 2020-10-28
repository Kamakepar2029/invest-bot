# -*- coding: utf-8 -*-
import telebot
import config
import subprocess
import os
import sys
import alls
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('💰 Balance', '💵 Withdraw','➕ Deposit')
    keyboard.row('🏷 Add Wallet','👨‍👦‍👦 Support','💬 Help')
    bot.send_message(message.chat.id, 'Hello! You have won '+config.start_balance+' '+config.currency, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def lalala(message):
  if (message.text == '💰 Balance'):
    bot.send_message(message.chat.id, 'Your Balance is:\n'+config.start_balance+' '+config.currency)

  elif (message.text == '💵 Withdraw'):
    bot.send_message(message.chat.id, 'To withdraw, you need to deposit at least '+config.withdraw+' '+config.currency+' with comment '+str(message.chat.id)+' .')

  elif (message.text == '👨‍👦‍👦 Support'):
    bot.send_message(message.chat.id, 'Our help is here: '+config.help_bots)

  elif (message.text == '💬 Help'):
    bot.send_message(message.chat.id, 'Our help is here: '+config.help_bots)

  elif (message.text == '➕ Deposit'):
    bot.send_message(message.chat.id, 'To deposit please send money in '+config.currency+' to '+config.wallet)

  elif (message.text == '🏷 Add Wallet'):
    bot.send_message(message.chat.id, 'You can add walllet only after first deposit')
  else:
    u = "Don't understand you. Your message was: "+str(message.text)
    bot.send_message(message.chat.id, u)
try:
  bot.polling(none_stop=True)
  pass
except:
  pass