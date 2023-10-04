import discord
import os
import random


intents = discord.Intents.default()
intents.typing = False  # Disable typing events
intents.presences = False  # Disable presence events

#connection to discord
client = discord.Client(intents=intents)
#register an event
@client.event

async def on_ready():

  print('login successful as {0.user}'.format(client))  

@client.event
async def on_message(message):
  if message.content.startswith('/supermario'):
    print('game running....')  


#my_secret = os.environ['token']

#client.run(my_secret)


