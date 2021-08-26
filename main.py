import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

import os

from keep_alive import keep_alive
from art import chat_with_ai

intents = discord.Intents.default()
intents.members = True

bot_prefix = '*cb ' # Bot Prefix

client = commands.Bot(command_prefix=bot_prefix,intents=intents)

@client.event
async def on_ready():
    print('Yellloo Coldi bot is here', client.user)
  
@client.command()
async def hello(ctx):
  await ctx.send("Hello")

@client.command(pass_context=True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    f = str(channel)
    await ctx.send('ColdiBOT has joined the Voice Channel '+f)
  else:
    await ctx.send('You have to join a voice channel first to use this command')

@client.command(pass_context=True)
async def play(ctx):
  if (ctx.voice_client):
    voice = ctx.channel.guild.voice_client
    print(type(ctx.voice_client))
    source = FFmpegPCMAudio('sounds/lick.mp3')
    player = voice.play(source)
    await ctx.send('Now playing the lick')
  else:
    await ctx.send('You have to join a voice channel first to use this command')

@client.command(pass_context=True)
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
    await ctx.send('Audio Paused')
  else:
    await ctx.send('ColdiBOT is not playing anything')

@client.command(pass_context=True)
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
    await ctx.send('Audio Resumed')
  else:
    await ctx.send('Audio is already playing')

@client.command(pass_context=True)
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  voice.stop()

@client.command(pass_context=True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Disconnected")
  else:
    await ctx.send('The bot is not in any voice channel')

@client.command()
async def hi(ctx):
  await ctx.send("Hello,ColdiBot to your service")

@client.command()
async def what(ctx):
  await ctx.channel.send(file=discord.File('gifs/giphy_what.gif'))

@client.command()
async def ai(ctx):
  question = ctx.message.content.split(bot_prefix)[1]
  answer = chat_with_ai(question,ctx.author)
  await ctx.send(answer)

keep_alive() #Fucntion to keep the bot running all the time

# Token to run the bot
TOKEN = os.environ['TOKEN']
client.run(TOKEN)