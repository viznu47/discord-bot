import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='.', intents= discord.Intents.all())
@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")

bot_id = os.getenv("bot_id")
bot.run(bot_id)

