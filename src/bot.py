import os
import discord
import logging
import pandas as pd
import yaml

logging.basicConfig(level=logging.INFO)
client = discord.Client()
guild = discord.Guild
data_folder = os.path.join("./src/data/")
with open("config.yml", "r") as f:
    config = yaml.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('Waiting patiently...'))
    print("Scraping messages...")
    await retrieve_messages()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('_'):

        cmd = message.content.split()[0].replace("_", "")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:]

async def retrieve_messages():
    data = pd.DataFrame(columns=['content', 'time', 'author'])
    channels = [chan for chan in client.get_all_channels() if str(chan.type) == "text"]

    for channel in channels:
        limit = 1000
        async for msg in channel.history(limit=limit + 1000):  # The added 1000 is so in case it skips messages for being
            if msg.author != client.user:  # a command or a message it sent, it will still read the
                data = data.append({'content': msg.content,
                                    'time': msg.created_at,
                                    'author': msg.author.name,
                                    'channel': channel.name}, ignore_index=True)
                if len(data) == limit:
                    break

    # Turning the pandas dataframe into a .csv file and sending it to the user
    file_location = f"{str(data_folder)}{guild.name}.csv"  # Determining file name and location
    # TODO: Figure out why this isn't actually the name of the guild
    data.to_csv(file_location)  # Saving the file as a .csv via pandas

    logging.info("Saved raw chat transcript at {}".format(file_location))

def initialize_bot():
    client.run(config["DISCORD_TOKEN"])
