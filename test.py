# https://alphalog.co.kr/212
import discord
import yaml

# YAML 파일 읽기
with open('./token_channel-id.yaml', 'r') as file:
    config = yaml.safe_load(file)

# token과 channel 값 가져오기
TOKEN = config['private']['token']
CHANNEL_ID = config['private']['channel']

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        await channel.send('Hello World')
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)