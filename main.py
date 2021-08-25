import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Yellloo Coldi bot is here',client)

@client.event
async def on_message(message):
  
  command = message.content
  if command.startswith('$kb'):

    command = message.content.split('*cb ')

    if message.author == client.user:
      return None
    
    if command[1] == ('hi'):
      await message.channel.send("ColdiBot to your service")

# Token to run the bot
TOKEN = os.environ['TOKEN']
client.run(TOKEN)