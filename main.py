from keepwake import keep_alive
from howdolist import howdolist
import discord
import os
client = discord.Client()
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('List'):
    
    await message.channel.send(howdolist(message))
  
keep_alive()
client.run(os.getenv('TOKEN'))