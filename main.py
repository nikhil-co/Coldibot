import discord

import os

from keep_alive import keep_alive
from art import chat_with_ai

client = discord.Client()

@client.event
async def on_ready():
    print('Yellloo Coldi bot is here', client)

@client.event
async def on_message(message):
    pre_commands = {'hi': 'Returns a welcome message'}
    command = message.content

    if command.startswith('*cb'):

        command = message.content.split('*cb ')

        if message.author == client.user:
          return None

        elif command[1] == ('hi'):
          await message.channel.send("ColdiBot to your service")
          return None

        elif command[1] == ('what'):
          await message.channel.send(file=discord.File('gifs/giphy_what.gif'))
          return None

        elif command[1].startswith('ai'):
          question = command[1].split('ai ')[1]
          await message.channel.send(chat_with_ai(question))

        else:
            await message.channel.send("The command " + command[1] +
                                       " not available")
            await message.channel.send("Commands that are avalaible: ")
            ans = str(pre_commands).replace("{", "").replace("}", "").replace(
                '"', "").replace(",", "").replace("'","")

            await message.channel.send(ans)
            return None

keep_alive() #Fucntion to keep the bot running all the time

# Token to run the bot
TOKEN = os.environ['TOKEN']
client.run(TOKEN) 

