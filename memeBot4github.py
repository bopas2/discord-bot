import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from PIL import Image, ImageDraw, ImageFont

#bot for making mark memes made by tommy

Client = discord.Client();
client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("BOT READY")

@client.command(pass_context=True)
async def t(ctx, *, message: str):
    msgArray = message.split()

    base = Image.open("C:\\Python\\markBot\\markTrump.png").convert('RGBA')
    fnt = ImageFont.truetype("C:\\Python\\markBot\\CONSOLA.TTF", 16)
    
    textFilter = Image.new('RGBA', base.size, (255,255,255,0))
    canvas = ImageDraw.Draw(textFilter)

    #for wrapping text around sign
    leng = len(message)
    if leng > 240:
        await client.say("message longer than 240 characters")
    else:
        charCount = 0
        rowCount = 0
        stringToWrite = ""
        for val in msgArray:
            if ((charCount + 1 + len(val) - rowCount * 30) < 30):
                stringToWrite += val + " "   
            else:
                canvas.text((210,295 + rowCount * 20), stringToWrite, font=fnt, fill='White')
                stringToWrite = val + " "
                rowCount = rowCount + 1
            charCount += len(val) + 1
        canvas.text((210,295 + rowCount * 20), stringToWrite, font=fnt, fill='White')

    out = Image.alpha_composite(base, textFilter.rotate(1*1.8))
    out.save("meme.png","PNG")

    await client.send_file(ctx.message.channel, 'meme.png')

client.run("TOKEN");
