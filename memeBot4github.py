import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from PIL import Image, ImageDraw, ImageFont
import time

#bot for making mark memes made by tommy

Client = discord.Client();
client = commands.Bot(command_prefix='bopas ')
client.remove_command('help')
msgLastSentWhen = -5

@client.event
async def on_ready():
    print("BOT READY")

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        description="Description of Bopas Bot's Capabilities",
        color=0x00ff00
    )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/140564130489696256/478291283190743052/unknown.png")
    embed.set_author(name='Bopas Bot Help',
                     icon_url="https://cdn.discordapp.com/attachments/140564130489696256/478291283190743052/unknown.png")
    embed.add_field(name="markSign", value="Make Mark hold a sign with a message of your choosing. Call using 'bopas markSign' and then type your message.", inline=True)
    embed.add_field(name="snowfishSign", value="Make snowfish hold a sign with a message of your choosing. Call using 'bopas snowfishSign' and then type your message.", inline=True)
    await client.say(embed=embed) 

@client.command(pass_context=True)
async def markSign(ctx, *, message: str):
    msgArray = message.split()

    base = Image.open("C:\\Python\\markBot\\markTrump.png").convert('RGBA')
    fnt = ImageFont.truetype("C:\\Python\\markBot\\CONSOLA.TTF", 16)
    
    textFilter = Image.new('RGBA', base.size, (255,255,255,0))
    canvas = ImageDraw.Draw(textFilter)

    #for wrapping text
    leng = len(message)
    charPerLine = 30
    if leng > 240:
        await client.say("message longer than 240 characters")
    else:
        charCount = 0
        rowCount = 0
        stringToWrite = ""
        for val in msgArray:
            if ((charCount + 1 + len(val) - rowCount * charPerLine) < charPerLine):
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

@client.command(pass_context=True)
async def snowfishSign(ctx, *, message: str):
    msgArray = message.split()

    base = Image.open("C:\\Python\\markBot\\snowTrump.png").convert('RGBA')
    fnt = ImageFont.truetype("C:\\Python\\markBot\\CONSOLA.TTF", 32)
    
    textFilter = Image.new('RGBA', base.size, (255,255,255,0))
    canvas = ImageDraw.Draw(textFilter)

    #for wrapping text
    leng = len(message)
    charPerLine = 19
    maxLength = charPerLine * 7
    if leng > maxLength:
        await client.say("message longer than " + str(maxLength) + " characters")
    else:
        charCount = 0
        rowCount = 0
        stringToWrite = ""
        for val in msgArray:
            if ((charCount + 1 + len(val) - rowCount * charPerLine) < charPerLine):
                stringToWrite += val + " "   
            else:
                canvas.text((265,315 + rowCount * 35), stringToWrite, font=fnt, fill='White')
                stringToWrite = val + " "
                rowCount = rowCount + 1
            charCount += len(val) + 1
        canvas.text((265,315 + rowCount * 35), stringToWrite, font=fnt, fill='White')
        out = Image.alpha_composite(base, textFilter.rotate(1*3))
        out.save("meme2.png","PNG")
        await client.send_file(ctx.message.channel, 'meme2.png')

@client.event
async def on_message(message):
    global msgLastSentWhen
    await client.process_commands(message)
    if message.author == client.user:
        return
    elif message.author.bot:
        return
    else:
        msg = message.content.lower()
        if " thot " in msg or " thot" in msg or "thot" in msg:
            localtime = time.localtime(time.time()).tm_min 
            if abs(localtime - msgLastSentWhen) >= 2:
                await client.send_message(message.channel,"if she breathes, she's a ***THOT***")
                msgLastSentWhen = localtime
    

client.run("token");
