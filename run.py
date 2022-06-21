# -*- coding: utf-8 -*-
import asyncio
import discord
import os
from discord.ext import commands
import json
import youtube_dl


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
    bot = commands.Bot(command_prefix="~~", status=discord.Status.online, activity=game)
    
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
        
        if text == "[도움말]" or text == "<도움말>":
            ctx = await bot.get_context(message)
            await help_message(ctx)
    
    async def send_image(ctx, img_name):
        await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
        await ctx.send(content=f"{ctx.author.nick if ctx.author.nick else ctx.author.name}:",
                       file=discord.File("emoji/"+img_name))
    
    async def help_message(ctx):
        await ctx.send(content=", ".join(command_data.keys()))
    
    @bot.command()
    async def play(ctx, url):
        channel = ctx.author.voice.channel
        if bot.voice_clients == []:
            await channel.connect()
            await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))
    
        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    
    @bot.command()
    async def pause(ctx):
        if not bot.voice_clients[0].is_paused():
            bot.voice_clients[0].pause()
        else:
            await ctx.send("already paused")
    
    @bot.command()
    async def resume(ctx):
        if bot.voice_clients[0].is_paused():
            bot.voice_clients[0].resume()
        else:
            await ctx.send("already playing")
    
    @bot.command()
    async def stop(ctx):
        if bot.voice_clients[0].is_playing():
            bot.voice_clients[0].stop()
        else:
            await ctx.send("not playing")    
    
    @bot.command()
    async def leave(ctx):
        await bot.voice_clients[0].disconnect()
    
    bot.run(os.environ['token'])
except Exception as e:
    print(e)
