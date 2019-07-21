from discord.ext import commands
import creds

client = commands.Bot(command_prefix = '.')
cryGif = 'https://giphy.com/gifs/cry-baby-TL2Yr3ioe78tO'

@client.event
async def on_ready():
    print('Bot is Ready')


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    authorID = message.author.id
    print('{}: {}, {}, {}'.format(author, content, channel, authorID))
    if str(authorID) in creds.usersCry:
        print('Yes')
        await message.channel.send(cryGif)

    elif author not in creds.usersCry:
        print('No')

client.run(creds.tokenID)