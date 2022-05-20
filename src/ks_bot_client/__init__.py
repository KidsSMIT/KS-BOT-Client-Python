# Version of the KS_Bot_Client package
__version__ = "2.5.1"

try:
  from ..ks_bot_client.bot import Bot
except:
  from ks_bot_client.bot import Bot

if __name__ == "__main__":
  bot =  Bot("<username>", "<password>")
  bot.run()
