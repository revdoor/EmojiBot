# -*- coding: utf-8 -*-
import asyncio
import discord
import os
from discord.ext import commands
import json


def command_match(text, command_data):
    for key in command_data.keys():
        length = len(key)
        
        if len(text) != length:
            continue
        
        if text == key:
            return True, key
    
    return False, None


try:
    game = discord.Game("로아 이모티콘")
    bot = commands.Bot(command_prefix="[", status=discord.Status.online, activity=game)
    
    with open("command.json", "r") as json_file:
        command_data = json.load(json_file)
    
    @bot.event
    async def on_ready():
        print("Starting bot")
    
    @bot.event
    async def on_message(message):
        text = message.content
        
        res, key = command_match(text, command_data)
        
        if res:
            ctx = await bot.get_context(message)
            await send_image(ctx, command_data[key])
        
        else:
            await bot.process_commands(message)
    
    async def send_image(ctx, img_name):
        await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
        await ctx.send(f"{ctx.author.nick if ctx.author.nick else ctx.author.name}:")
        await ctx.send(file=discord.File("emoji/"+img_name))

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
