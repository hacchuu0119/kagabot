# coding: UTF-8

import SearchGeneral
import discord  # インストールした discord.py
import asyncio
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', help='Disignate the access token to connect to your discord bot')
args = parser.parse_args()

client = discord.Client()  # 接続に使用するオブジェクト


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    # 発言ユーザが自分の場合return
    if client.user == message.author: return
    bot_reply = SearchGeneral.ReplyClass(message.content)
    if bot_reply.full_text_match() is not None:
        print(bot_reply.full_text_match())
        reply = bot_reply.full_text_match()
        await client.send_message(message.channel, reply)

    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)

    if message.content.startswith('/waku'):
        reply = 'waku'
        await client.send_message(message.channel, reply)

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    if client.user.id in message.content:
        print(message.author.mention)
        # 自分用
        if message.author.mention == "<@330411083980603394>":
            reply = f'お呼びですか、{message.author.mention} 様！'
        # シエルさん
        elif message.author.mention == "<@294059343068921857>":
            reply = f'(何言ってんだ、{message.author.mention} ？？)'
        #
        elif message.author.mention == "<@301692231775944716>":
            reply = f'あ、{message.author.mention}だ！ かわいい！SS撮ろ！'
        else:
            reply = f'{message.author.mention}さん、なにかご用ですか？'
        print(reply)
        await client.send_message(message.channel, reply)


# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run(args.token)
