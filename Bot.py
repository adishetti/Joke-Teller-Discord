from time import time, ctime
import discord
import pyjokes
import responses
from _multiprocessing import send


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author, send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTAyMDg0NjM0OTc1NjkyNDAyNQ.GKrCNQ.2BIpQznT5JpUYOvrbX2baH-yr7LctQJO_1WpY8'
    INTENTS = discord.Intents.all()
    client = discord.Client(intents=INTENTS)

    @client.event
    async def on_ready(GUILD=None):
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

    @client.event
    async def on_message(message, en=None):
        if message.author == client.user:
            return

        if message.content == '!joke':
            # response = random.choice(joke)
            response = pyjokes.get_joke()
            await message.channel.send(response)

        if message.content == '!time':
            t = time()
            response1 = ctime(t)
            await message.channel.send(response1)

        if message.content == '!help':
            response2 = "!joke tells you a joke, !time tells you the time, and !help tells you this message."
            await message.channel.send(response2)

    client.run(TOKEN)
