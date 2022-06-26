# -*- coding: utf-8 -*-
import asyncio
import discord
import os
from discord.ext import commands
import json
import youtube_dl
import random


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
            return
        
        if text == "[도움말]" or text == "<도움말>":
            ctx = await bot.get_context(message)
            await help_message(ctx)
            return
        
        await bot.process_commands(message)
    
    async def send_image(ctx, img_name):
        await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
        await ctx.send(content=f"{ctx.author.nick if ctx.author.nick else ctx.author.name}:",
                       file=discord.File("emoji/"+img_name))
    
    async def help_message(ctx):
        await ctx.send(content=", ".join(command_data.keys()))
    
    @bot.command()
    async def join(ctx):
        if not ctx.author.voice:
            await ctx.send("사용자가 음성 채널에 연결되어 있지 않습니다")
            return
        
        channel = ctx.author.voice.channel
        bot.queue = {}
        await ctx.send(f"{channel} 음성 채널에 연결하였습니다")
        await channel.connect()
    
    @bot.command()
    async def play(ctx, url):
        if bot.voice_clients == []:
            await bot.join(ctx)
        
        try:
            ydl_opts = {'format': 'bestaudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
            voice = bot.voice_clients[0]
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        except:
            await ctx.send("문제가 발생하였습니다. 다시 시도해주세요")
    
    @bot.command()
    async def pause(ctx):
        if not bot.voice_clients[0].is_paused():
            bot.voice_clients[0].pause()
        else:
            await ctx.send("이미 일시정지된 상태입니다")
    
    @bot.command()
    async def resume(ctx):
        if bot.voice_clients[0].is_paused():
            bot.voice_clients[0].resume()
        else:
            await ctx.send("이미 재생 중입니다")
    
    @bot.command()
    async def skip(ctx):
        if bot.voice_clients[0].is_playing():
            bot.voice_clients[0].stop()
        else:
            await ctx.send("재생 중이 아닙니다")
    
    @bot.command()
    async def leave(ctx):
        await bot.voice_clients[0].disconnect()
        await ctx.send("봇 연결이 해제되었습니다")
    
    @bot.command(aliases=["뽑기"])
    async def draw(ctx, draw_no, *names):
        try:
            draw_no = int(draw_no)
            
            await ctx.send("{}에서 {}개를 뽑습니다.\n뽑은 값들은 {}입니다.".format(names, draw_no,
                                                                                   " ".join([random.choice(names) for _ in range(draw_no)])))
    
    bot.run(os.environ['token'])
except Exception as e:
    print(e)
