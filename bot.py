import discord
# from discord.ext import commands

Token = 'OTAwNTk0MzE0Njg4NzI5MTQ4.YXDl0A.BDMwZZ-d_M5m5j663wD7IdzTvxA'

# bot = commands.Bot(command_prefix='!')



client = discord.Client()

@client.event
async def on_ready():
    print('hi')
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to this Pro Server')

@client.event
async def on_message(message):
    print(message.author)

    if message.content == '!helloWin':
        await message.channel.send('I know this guy, BOONNIM right?')

client.run(Token)