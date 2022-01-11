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
    
    async def send_image(ctx, img_name):
        await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
        await ctx.send(f"{ctx.author.nick if ctx.author.nick else ctx.author.name}:")
        await ctx.send(file=discord.File("emoji/"+img_name))
    
    bot.run(os.environ['token'])
except Exception as e:
    print(e)
