import discord # インストールした discord.py
import asyncio
client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
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
        if (message.author.mention == "<@330411083980603394>"):
            reply = f'{message.author.mention} 様！好きです！'

        elif(message.author.mention == "<@294059343068921857>"):
            reply = f'(何言ってんだ、{message.author.mention} ？？)'
        else:
            reply = f'{message.author.mention} 呼んだ？？'
        print(reply)
        echo_method(reply)
        await client.send_message(message.channel, reply)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NDg3NjEwODY5MTE1NzgxMTIx.DnQLQw.M0Fg5EOxeDsWvOtda7dq2ebQAgQ')