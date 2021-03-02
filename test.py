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


client.run('ODE1OTA2Mjg3ODk2MjMxOTM3.YDzN8Q.zgEy37pxOX8RKjVhGa31GwSHZHw')