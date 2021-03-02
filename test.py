import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def clear(ctx, number):
    number = int(number)
    counter = 0
    if counter < number:
        await ctx.channel.purge(limit=number)
        counter += 1


client.run('TOKEN')
