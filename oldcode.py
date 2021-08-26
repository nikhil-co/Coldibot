pre_commands = {'hi': 'Returns a welcome message',
                'ai': 'Answers any question or completes any sentence - uses Open AI'}

@client.command()
async def hi(ctx):
  await ctx.send("Hello,ColdiBot to your service")

@client.command()
async def what(ctx):
  await ctx.channel.send(file=discord.File('gifs/giphy_what.gif'))

@client.command()
async def ai(ctx):
  

async def on_message(message):
    command = message.content

    if command.startswith('*cb'):

        command = message.content.split('*cb ')
        if command[1]==None:
          return None

        elif command[1] == ('hi'):
          await message.channel.send("ColdiBot to your service")
          return None

        elif command[1] == ('what'):
          await message.channel.send(file=discord.File('gifs/giphy_what.gif'))
          return None

        elif command[1].startswith('ai'):
          question = command[1].split('ai ')[1]
          await message.channel.send(chat_with_ai(question,message.author))

        else:
            await message.channel.send("The command " + command[1] +
                                       " not available")
            await message.channel.send("Commands that are avalaible: ")
            ans = str(pre_commands).replace("{", "").replace("}", "").replace(
                '"', "").replace(",", "").replace("'","")

            await message.channel.send(ans)
            return None
