import discord
import random
from discord.ext import commands
import googletrans
from googletrans import Translator


client = commands.Bot(command_prefix = '.')
client.remove_command('help')
bot = commands.Bot(...)
bot.message = 0

@client.event
async def on_ready():
    print(f'Ready!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ({round(client.latency * 1000)}ms)')
    
@client.command(aliases = ['8ball'])
async def eightball(ctx):
    x = random.randint(1,17)
    f = open('8ball.txt')
    lines = f.readlines()
    await ctx.send(f'{(lines[x])}')
    
@client.command(aliases = ['wyr'])
async def wouldyourather(ctx):
    x = random.randint(1,31)
    f = open('wyrtext.txt')
    lines=f.readlines()
    await ctx.send(f'{(lines[x])}')

    await ctx.send(f'{random.choice(responses)}')
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    if reason == None:
        await ctx.send(f'{member.name} has been kicked')
    else:
        await ctx.send(f'{member.name} has been kicked because {reason}')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def translate(ctx, arg, arg2):
    translator = Translator()
    result = translator.translate(arg, dest=arg2)
    await ctx.send(f'{result.text}')

@client.command()
async def help(ctx):
    await ctx.send(f'''
        .ping: Shows the latency of the bot
.wyr: Shows a would you rather question
.8ball: Harnesses the power of the magic 8ball to tell you your future
.translate: Uses the google translate API to let you translate anything into any language using discord.(Kinda proud of this one)
.help: What you're looking at now
    
Support server: https://discord.gg/TE5Hwaz
Created by ZizOhNo#1012''')
@client.command()
async def setjoinmessage (ctx, *, message=None):
        bot.message = message
        await ctx.send(f'''The message is "{bot.message}"''')

@client.event
async def on_member_join(member):
    if bot.message == None:
        pass
    else:
        await member.send(f'{bot.message}')
    





client.run('TOKEN')

