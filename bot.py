import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='>>')

@bot.event
async def on_connect():
    print('>>我就爛已上線 恩~ 好啦閉嘴啦<<')

async  def on_ready():
    print('已上線')

@bot.event
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("好啦 閉嘴啦")
      else:
        await message.channel.send(tmp[1])
bot.run('OTM4NDIwNDUzNDMxNzM0MzE2.YfqCJw.kGAw2YCqbNv7YRjfeebr8q0f2Ng')