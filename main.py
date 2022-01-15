#pip install git+https://github.com/Jadtz/quran.py.git
from Keep_alive import keep_alive
import discord
from discord.ext import commands
from ayat import *
import os
from fillin_aya import *

client = commands.Bot(command_prefix='$')

@client.command()
async def ping(ctx):
  await ctx.send("pong")

@client.command()
async def verse(ctx,id):
    embed = discord.Embed(
      title="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
      description = f"\n\n**{nav_verse(id)}**",
      color = discord.Colour.blue()
    )
    
    await ctx.send(embed=embed)

@client.command()
async def test(ctx,id):
  verse = chapter_test(id)
  embed = discord.Embed(
    title="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    description = f"{verse[0]}({verse[1]})",
    color = discord.Colour.blue()
    )
  
  await ctx.send(embed=embed)
  

client.run(os.environ['TOKEN'])
keep_alive()