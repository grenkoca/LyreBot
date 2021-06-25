import discord
import os
import getpass
import yaml

client = discord.Client()

def initialize_bot(config):
    token = config["TOKEN"]
    client.run(token)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

