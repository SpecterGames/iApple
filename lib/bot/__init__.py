from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Intents
from discord import Embed

PREFIX = "?"
OWNER_IDS = [672426611945242625]


class Bot(BotBase):

	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX,
		                 owner_ids=OWNER_IDS,
		                 intents=Intents.all())

	def run(self):
		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("Running bot!")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("Bot connected!")

	async def on_disconnect(self):
		print("Bot disconnected!")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(1075793014393413822)
			channel = self.get_channel(1075794251180421211)

			embed = Embed(title="iApple (STILL IN DEVELOPMENT)",
			              description="Bot (iApple) is now online!")

			await channel.send("Bot is online!")
			print("Bot ready!")
		else:
			print("Bot reconnected!")

	async def on_message(self, message):
		pass


bot = Bot()
