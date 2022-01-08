# -*- coding: utf-8 -*-
import asyncio
import discord
import os
import random
from discord.ext import commands

try:
    dirname = os.path.dirname(os.path.abspath(__file__))
    
    game = discord.Game("로아 이모티콘")
    bot = commands.Bot(command_prefix="[", status=discord.Status.online, activity=game)
    
    @bot.event
    async def on_ready():
        print("Starting bot")
    
    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
    
    async def send_image(ctx, img_name):
        await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
        await ctx.send(f"{ctx.author.nick if ctx.author.nick else ctx.author.name}:")
        await ctx.send(file=discord.File(dirname+"/emoji/"+img_name))
    
    @bot.command(name="놀자에요]")
    async def letsplay(ctx):
        await send_image(ctx, "놀자에요_half.png")

    @bot.command(name="요에자놀]", aliases=["놀자에요반전]"])
    async def letsplay_flip(ctx):
        await send_image(ctx, "놀자에요_half_transpose.png")
    
    @bot.command(name="놀자에몽]")
    async def letsplay_dream(ctx):
        await send_image(ctx, "놀자에몽_half.png")
    
    @bot.command(name="머쓱해요]")
    async def shy(ctx):
        await send_image(ctx, "머쓱해요_half.png")
    
    @bot.command(name="웃프네요]")
    async def funsad(ctx):
        await send_image(ctx, "웃프네요_half.png")
    
    @bot.command(name="추천이요]")
    async def thumbsup(ctx):
        await send_image(ctx, "추천이요_half.png")
    
    @bot.command(name="정말이요]")
    async def really(ctx):
        await send_image(ctx, "정말이요_half.png")
    
    @bot.command(name="뭐라구요]")
    async def whatareyousaying(ctx):
        await send_image(ctx, "뭐라구요_half.png")
    
    @bot.command(name="머쓱환에요]")
    async def shy_dream(ctx):
        await send_image(ctx, "머쓱환에요_half.png")
    
    @bot.command(name="웃기구요]")
    async def realfun(ctx):
        await send_image(ctx, "웃기구요_half.png")

    @bot.command(name="엄지로아콘]", aliases=["엄지척]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_01_따봉_modified.png")
        
    @bot.command(name="야호로아콘]", aliases=["모야호]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_03_모야호_modified.png")
        
    @bot.command(name="크크로아콘]", aliases=["크크크]", "ㅋㅋㅋ]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_06_ㅋㅋㅋㅋ_modified.png")
        
    @bot.command(name="방긋로아콘]", aliases=["방긋]", "방긋방긋]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_09_방긋_modified.png")
        
    @bot.command(name="해줘로아콘]", aliases=["해줘]", "줘]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_13_줘_modified.png")
        
    @bot.command(name="안줘로아콘]", aliases=["안줘]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_14_안_줘_modified.png")
        
    @bot.command(name="빠직로아콘]", aliases=["빠직]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_17_빠직_modified.png")
        
    @bot.command(name="슬퍼로아콘]", aliases=["슬퍼]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_18_슬퍼_modified.png")
        
    @bot.command(name="향기로아콘]", aliases=["향기]", "기분좋은향기]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_23_향기_modified.png")
    
    @bot.command(name="털썩로아콘]", aliases=["털썩]"])
    async def loacon_thumbs(ctx):
        await send_image(ctx, "01_모코코콘1_24_모무룩_modified.png")

    @bot.command(name="기도해욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤1_modified.png")

    @bot.command(name="빼꼼이욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤5_modified.png")

    @bot.command(name="발사해욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤2_modified.png")

    @bot.command(name="불만이욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤6_modified.png")

    @bot.command(name="맛있어욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤3_modified.png")

    @bot.command(name="피곤해욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤7_modified.png")

    @bot.command(name="니야호욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤4_modified.png")

    @bot.command(name="큰일이욤]")
    async def ninab_pray(ctx):
        await send_image(ctx, "니나브욤8_modified.png")
    
    bot.run(os.environ['token'])
except Exception as e:
    print(e)
