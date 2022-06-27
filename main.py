import telegram
import passWord

token = passWord.tele_offline_run_token
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)