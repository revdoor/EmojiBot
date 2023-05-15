# -*- coding: utf-8 -*-
import asyncio
import discord
import os
from discord.ext import commands
import json
import youtube_dl
import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_data = json.loads(os.environ['json'])
credentials = ServiceAccountCredentials.from_json_keyfile_dict(json_data, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = os.environ['spreadsheet']
doc = gc.open_by_url(spreadsheet_url)

manager = json.loads(os.environ['manager'])


def get_command_info():
    global command_data
    
    command_no = int(doc.worksheet('number').acell('A1').value)
    
    command_raw = doc.worksheet('command').range(f'A1:B{command_no}')
    
    for i in range(command_no):
        name = command_raw[2*i].value
        url = command_raw[2*i+1].value
        
        command_data[name] = url


try:
    game = discord.Game("로아 이모티콘")
    bot = commands.Bot(command_prefix="~~", status=discord.Status.online, activity=game,
                       intents=discord.Intents.default())
    
    command_data = dict()

    get_command_info()

    @bot.event
    async def on_ready():
        print("Starting bot")

    @bot.event
    async def on_message(message):
        global command_data
        
        ctx = await bot.get_context(message)
        text = message.contentr

        if text in command_data:
            await ctx.channel.purge(limit=1, check=lambda m: m.author == ctx.author)
            await ctx.send(f"{ctx.author.nick if ctx.author.nick else ctx.author.name}:")
            await ctx.send(command_data[text])
            return

        if text == "[도움말]" or text == "<도움말>":
            await help_message(ctx)
            return
        
        if text == "리로드" and ctx.author.name in manager:
            command_data = dict()
            await get_command_info()

        await bot.process_commands(message)

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
            
            await ctx.send("{} 중에서 {}개를 뽑습니다.\n뽑은 값{}은 <{}>입니다.".format(" ".join(list(names)), draw_no,
                                                                                        "들" if draw_no > 1 else "",
                                                                                        " ".join([random.choice(names) for _ in range(draw_no)])))
        except:
            pass

    bot.run(os.environ['token'])

except Exception as e:
    print(e)
