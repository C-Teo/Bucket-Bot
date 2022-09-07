import discord
from discord.ext import commands
import dotenv
import logging

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"We have logged in as {client.user}")
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send("Hello!")

        if message.content.startswith('!test'):
            await message.channel.send("Test!")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot('$', intents=intents)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client = MyClient(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def double(ctx: commands.Context, number: float):
    await ctx.send(number * 3)

bot.run(dotenv.dotenv_values().get('TOKEN'), log_handler=handler)