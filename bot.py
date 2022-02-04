import discord
import time
import random
import json
from discord.ext import commands

#with open('setting.json','r',encoding='utf8') as jfile:
    #jdata = json.load(jfile)

bot = commands.Bot(command_prefix='>>')

@bot.command()
async def yong(ctx):
    pic1 = discord.File('C:\\Users\\William\\Documents\\GitHub\\DC_bot\\pic\\1.jpg')
    await ctx.send(file= pic1)

@bot.command()
async def tsai(ctx):
    pic1 = discord.File('C:\\Users\\William\\Documents\\GitHub\\DC_bot\\pic\\3.jpg')
    await ctx.send(file= pic1)
@bot.command()
async def yan(ctx):
    pic1 = discord.File('C:\\Users\\William\\Documents\\GitHub\\DC_bot\\pic\\2.jpg')
    await ctx.send(file= pic1)
@bot.command()
async def yellow(ctx):
    pic1 = discord.File('C:\\Users\\William\\Documents\\GitHub\\DC_bot\\pic\\4.jpg')
    await ctx.send(file= pic1)
@bot.command()
async def papig(ctx):
    pic1 = discord.File('C:\\Users\\William\\Documents\\GitHub\\DC_bot\\pic\\6.mp4')
    await ctx.send(file= pic1)
@bot.command()
async def gun(ctx):
    pic1 = discord.File('C:\\Users\\William\\Documents\\GitHub\\DC_bot\\pic\\5.jpg')
    await ctx.send(file= pic1)



@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)
@bot.event
async def on_connect():
    print('>>我就爛已上線 恩~ 好啦閉嘴啦<<')
@bot.event
async  def on_ready():
    print('已上線')
    game = discord.Game('遊戲王')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):

        #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    if message.content.startswith('說'):
          #分割訊息成兩份
        tmp = message.content.replace(' ','')
        tmp1 = message.content.split("說",2)
          #如果分割後串列長度只有1
        if len(tmp1) == 1:
            await message.channel.send("好啦 閉嘴啦")
        else:
            await message.channel.send(tmp1[1])
    if message.content.startswith('>>哪裡好吃'):
        await message.channel.send('屁眼')
    if message.content.startswith('機油'):
        await message.channel.send('好...難...喝...')
    if message.content.startswith('人都去哪了'):
        await message.channel.send('人都滾了= =')

    content = message.content.replace(' ','')
    if message.content.startswith('>>roll'):
        content = content.replace('>>roll','')
        dice_total = content.split('d')[1]
        try:
            tumple = ('```即將開始遊戲```')
            await message.channel.send(tumple)
            await message.channel.send('https://tenor.com/view/dice-gif-18958117')
            list1 = range(int(dice_total))
            list2 = [random.randint(1, 6) for _ in list1]
            list3 = [random.randint(1, 6) for _ in list1]
            count1 = 0
            for x in list2:
                count1 = count1 + x
            await message.channel.send('```您骰的結果為'+str(list2)+'總合為'+str(count1)+'```')
            computer_total = [random.randint(1, 7) for _ in list1]
            count2 = 0
            for x in list3:
                count2 = count2 + x
            await message.channel.send('```電腦骰的結果為' + str(list3) +'總合為'+str(count2)+ '```')
            if count2>count1:
                await message.channel.send('```你好可悲喔 人生輸 遊戲也輸```')
            elif count2==count1:
                await message.channel.send('```ㄏㄏ 盡然平手 你ㄇ確診```')
            else:
                await message.channel.send('```阿贏電腦是在高潮甚麼?```')
        except ValueError:
            await message.channel.send('```你媽教你數字這樣打?```')
    await bot.process_commands(message)
@bot.event
async def on_message_delete(deleted_message):
    await deleted_message.channel.send('又刪掉甚麼 = =')
    while deleted_message == '又刪掉甚麼 = =':
        break


@bot.event
async def on_typing(channel,user,when):
    print(channel)
    print(user)
    print(when)



#@bot.event
#async def on_typing(channel, user, when):
    #while True:
        #await channel.send('媽的 打字打快一點好不好啊')





bot.run('OTM4NDIwNDUzNDMxNzM0MzE2~YfqCJw.ImLmNnrlzhyp80uzjOhLlzgt1gU')