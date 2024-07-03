import discord
import random
import os
import requests

from discord.ext import commands
client = discord.Client()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.command 
async def help(ctx)
    await ctx.send('heh add roll repeat triple mem vp tv')

    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right) 

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def triple(ctx, z: int, x: int, c: int):
    await ctx.send(z + x + c)


@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    rand_image = random.choice(images)
    with open (f'images/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await  ctx.send(file=picture)

@bot.command()
async def vp(ctx, count = 1):
    await ctx.send ("2+2 45+22 12+12 100+10 15+5")
    
@bot.command()
async def   tv(ctx):
    await ctx.send ("4, 67, 24, 110 ,20")


@client.command()
async def rd(ctx):
rd = ["rg", "eny", "e"]
await ctx.send(f"{random.choice(random)}")

@client.command()
async def send(ctx, *, message: str):
    await ctx.send(message)


bot.run("")

