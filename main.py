import string
import discord
from discord.ext import commands
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

@bot.command()
async def double(ctx: commands.Context, number: float):
    await ctx.send(number * 3)

@bot.command()
async def meme(ctx: commands.Context, meme: str, *args):
    match meme.lower():
        case "lisa":
            # https://cdn.nathanferns.xyz/memes/lisa?
            await ctx.send("https://cdn.nathanferns.xyz/memes/lisa?text="+args[0])

        case "Office":
            await ctx.send("You specified: The Office")

        case _:
            await ctx.send("You sent nothing.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("That command wasn't found! Sorry :(")
        return
    elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send("Invalid arguements, sorry! :(")
        return
    await ctx.send("Another Problem has occured!")

bot.run(dotenv.dotenv_values().get('TOKEN'), log_handler=handler)