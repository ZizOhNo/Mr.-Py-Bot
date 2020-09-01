import discord
import random
from discord.ext import commands
import googletrans
from googletrans import Translator


client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Ready!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ({round(client.latency * 1000)}ms)')
@client.command(aliases = ['8ball'])
async def eightball(ctx):
    responses1 = ['It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes – definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't count on it.",
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.']
    await ctx.send(f'{random.choice(responses1)}')
@client.command(aliases = ['wyr'])
async def wouldyourather(ctx):
    responses =  ['Would you rather go into the past and meet your ancestors or go into the future and meet your great-great grandchildren?',
        'Would you rather have more time or more money?',
        'Would you rather have a rewind button or a pause button on your life?',
        'Would you rather be able to talk with the animals or speak all foreign languages?',
        'Would you rather win the lottery or live twice as long?',
        'Would you feel worse if no one showed up to your wedding or to your funeral?',
        'Would you rather be without internet for a week, or without your phone?',
        'Would you rather meet George Washington, or the current President?',
        'Would you rather lose your vision or your hearing?',
        'Would you rather work more hours per day, but fewer days or work fewer hours per day, but more days?',
        'Would you rather listen to music from the 70’s or music from today?',
        'Would you rather become someone else or just stay you?',
        'Would you rather be Batman or Spiderman?',
        'Would you rather be stuck on a broken ski lift or in a broken elevator?',
        'For your birthday, would you rather receive cash or gifts?',
        'Would you rather go to a movie or to dinner alone?',
        'Would you rather always say everything on your mind or never speak again?',
        'Would you rather make a phone call or send a text?',
        'Would you rather read an awesome book or watch a good movie?',
        'Would you rather be the most popular person at work or school or the smartest?',
        'Would you rather put a stop to war or end world hunger?',
        'Would you rather spend the night in a luxury hotel room or camping surrounded by beautiful scenery?',
        'Would you rather explore space or the ocean?',
        'Would you rather go deep sea diving or bungee jumping?',
        'Would you rather be a kid your whole life or an adult your whole life?',
        'Would you rather go on a cruise with friends or with your spouse?',
        'Would you rather lose your keys or your cell phone?',
        'Would you rather eat a meal of cow tongue or octopus?',
        'Would you rather have x-ray vision or magnified hearing?',
        'Would you rather work in a group or work alone?',
        'Would you rather be stuck on an island alone or with someone who talks incessantly?',
        'Would you rather be too hot or too cold?',
           'When you’re old, would you rather die before or after your spouse?']
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
async def setjoinmessage (ctx, arg, message=None):
    if message == None:
        await ctx.send(f'No message has been sent')
    else:
        await ctx.send(f'''The message is "{message}"''')



@client.event
async def on_member_join(member, message):
    if message == None:
        pass
        
    else:
        await member.send(f'{message}')

    





client.run('TOKEN')

