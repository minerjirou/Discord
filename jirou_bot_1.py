import discord
import datetime

# トークン
TOKEN = 'token'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('起動しました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # 「/nuko」と発言したら「にゃーん」が返る処理
    if message.content == '/nuko':
        await message.channel.send('にゃーん')
    # 「/nukko」と発言したら「にゃーん」が返る処理
    if message.content == '/nukko':
        await message.channel.send('にゃーん')
     # 「/pien」と発言したら「ぴえん」が返る処理
    if message.content == '/pien':
        await message.channel.send('ぴえん')
    #　時報処理
    if message.content == '/nt':
     time = datetime.datetime.now()
     await message.channel.send(time)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)