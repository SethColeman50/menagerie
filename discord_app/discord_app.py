import discord
from dotenv import load_dotenv
import os

# Get token to give to bot
load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello')


def main():
    try:
        client.run(token)
        print('Bot is running')

    except discord.errors.LoginFailure as e:
        print(e)
        print(token)
        print("Please check your token")
        exit(1)

if __name__ == "__main__":
    main()