import config
import os

def balance(userid):
  return (config.start_balance)

def add_wallet(wallet, chatid):
  os.system('echo "'+wallet+'">'+chatid+'.txt')
  return 'Wallet Added!'

def get_wallet(chatid):
  wallet = open(chatid+'.txt','r').read()
  return wallet