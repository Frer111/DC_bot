import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>>')

@bot.event
async def on_connect():
    print('>>我就爛已上線 恩~ 好啦閉嘴啦<<')

async  def on_ready():
    print('已上線')

bot.run('OTM4NDIwNDUzNDMxNzM0MzE2.YfqCJw.QqjjVwGpOkwtYdinZLYhcXFBM-Q')

