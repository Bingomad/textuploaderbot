import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
from get_video_info import get_video_attributes, get_video_thumb
import re
from pyrogram import Client as bot
DEF_FORMAT = "480"
from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
API_ID = 952608
API_HASH = "8d8d0ad8e3d4bcd54420190f57da78ad"
BOT_TOKEN = "6144745485:AAFFSe33wLuWwKAWMkau8mYopgJT0OoOCmE"
AUTH_USERS = 818269274
sudo_users = [818269274]
bot = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)
async def exec(cmd):
  proc = await asyncio.create_subprocess_exec(*cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
  stdout, stderr = await proc.communicate()
  print(stdout.decode())
  return proc.returncode,stderr.decode()
  
  
  
  
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
 editable = await m.reply_text("**Hi BOSS I'm Alive Send /down download and for classplus send /cpd  for /dhurina for /vision**")


          

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
    
    
    
    
@bot.on_message(filters.command(["cpd"]))
async def account_login(bot: Client, m: Message):
    
    editable = await m.reply_text("Send Classplus Links Text File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total **{len(links)}** Founded 🤷‍♂️\n\n Download Start From Which Link?.(Enter Line Number) \n\n If You Need To Download From First Then Enter Number 👉 **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Batch** 🥎")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter Resolution Quality**🥊")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    raw_text6 = "no"
    thumb = "no"
    res = "NA"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*","").replace("download",".pdf").replace(".","").strip()
            name = f'{str(count).zfill(3)}) {name1}'    
            print("❤") 


            
          
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            if "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
            elif "classplusapp" in url:
                print("❤❤") 
            	headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6ODg5NjE4NDMsIm9yZ0lkIjoyNTUxLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTY2NjMzMzY2NjU1OCIsIm5hbWUiOiJGZmZmZmZmIiwiZW1haWwiOiJsYWtlZm94NzA1QGxpZWJvZS5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOmZhbHNlLCJsb2dpblZpYSI6Ik90cCIsImZpbmdlcnByaW50SWQiOiJiNjY3M2Y1YjQ2NmNiODZmZGFhZmJlZGZjNzRjZWYzNSIsImlhdCI6MTY4MTIzMjExNywiZXhwIjoxNjgxODM2OTE3fQ.r0klWJjEaA2jqpij_aSGXA7Mth2rd6LEsfRUhZT8a0byvsJd811FUiyH3TnIfTev', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8fhb3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            	params = (('url', f'{url}'),)
            	response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            	url = response.json()['url']
            	cmd = f'yt-dlp -o "{name}.%(ext)s" --no-keep-video --remux-video mkv "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                if "classplus" in url:
                    cmd = f'yt-dlp --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                else:
                    cmd = f'yt-dlp -f "{ytf}" --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" or "download" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            print(cmd)
            print("❤❤❤") 
            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`"
                prog = await m.reply_text(Show)
                cc = f'{str(count).zfill(3)}**.** {name1} {res}\n**Batch :-** {raw_text0}'
                cc1 = f'{str(count).zfill(3)}**.** {name1} {res}.pdf\n**Batch :-** {raw_text0}'
                print("❤❤❤❤") 
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    try:
                        print("❤❤❤❤❤") 
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f'**Title »** {name1} {res}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
                        )
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    print("❤❤❤❤❤❤") 
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue
                print("❤❤❤❤❤❤❤") 

    except Exception as e:
        await m.reply_text(e)
        print("⚽⚽⚽⚽⚽⚽⚽") 
    await m.reply_text("Done")
    print("❤😡😡😡") 
    


    
    
bot.run()    




