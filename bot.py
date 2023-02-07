import logging
import logging.config

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

PORT = os.environ.get('PORT', '8080')

import os
from config import Config
from pyrogram import Client
from plugins.database import db 
from aiohttp import web
from route import web_server

class Bot(Client):
   
   def __init__(self):
       super().__init__(
            name="md-rename-bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={"root": "plugins"},
        )
      
   async def start(self):
      await super().start()
      self.log = logging
      if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
      banned_users = await db.get_banned_users()
      Config.BANNED_USERS = banned_users
      app = web.AppRunner(await web_server())
      await app.setup()
      bind_address = "0.0.0.0"       
      await web.TCPSite(app, bind_address, PORT).start()     
      print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")

   async def stop(self):
      await super().stop()
      logging.info(f"{self.me.first_name} is stopped...")

bot = Bot()
bot.run()
