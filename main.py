
import discord
from discord.ext import commands
from urllib.parse import quote
import dotenv
import logging

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot('$', intents=intents)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command() # Doubles the given Float
async def double(ctx: commands.Context, number: float):
    await ctx.send(number*2)

@bot.command() # Change My Mind Parameters -> [StrText]
async def changemymind(ctx: commands.Context, *, text: str):
    arr = convert_param(text)
    await ctx.send("https://mime.rcp.r9n.co/memes/changemymind?text="+arr[0])

@bot.command() # Clown Parameters -> [StrOne] [StrTwo] [StrThree] [StrFour]
async def clown(ctx: commands.Context, *, text: str):
    arr = convert_param(text)
    await ctx.send("https://cdn.nathanferns.xyz/memes/clown?one="+arr[0]+"&two="+arr[1]+"&three="+arr[2]+"&four="+arr[3])

@bot.command() # Office Parameters -> [Img] [Str] [Str] [Str] [Str] [Str]
async def office(ctx: commands.Context, *, text: str):
    arr = convert_param(text)
    await ctx.send(""+arr[0])

@bot.command() # Lisa Parameters -> [StrText]
async def lisa(ctx: commands.Context, *, text: str):
    arr = convert_param(text)
    await ctx.send("https://cdn.nathanferns.xyz/memes/lisa?text="+arr[0])

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("That command wasn't found! Sorry :(")
        return
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send("Invalid arguements, sorry! :(")
        return
    await ctx.send("Another Problem has occured!")

def convert_param(text: str):
    arr = text.split(',')
    for i in range(len(arr)):
        arr[i] = quote(arr[i])
    return arr

bot.run(dotenv.dotenv_values().get('TOKEN'), log_handler=handler)