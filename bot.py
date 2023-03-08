import os

import discord
import responses
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), 'secret.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("TOKEN")


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(message=user_message, author=message.author)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def handle_reaction_role(payload, add: bool = True):
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        emoji = payload.emoji.name
        channel = discord.utils.get(guild.channels, name='roles')
        channel_id = channel.id
        message_id = 1082389583632797706
        role = None

        if message_id == payload.message_id:
            if payload.channel_id == channel_id:
                # Doing it this way because emoji from payload has a weird whitespace character
                # if '\u2639'.encode('UTF-8') in emoji.encode('UTF-8'):
                if emoji == '👍':
                    role = discord.utils.get(guild.roles, name='Narys')
                if emoji == '👌':
                    role = discord.utils.get(guild.roles, name='Noob')
                if emoji == '🪓':
                    role = discord.utils.get(guild.roles, name='Maladec')
            if add:
                await member.add_roles(role)
            else:
                await member.remove_roles(role)

    @client.event
    async def on_raw_reaction_add(payload):
        await handle_reaction_role(payload, add=True)

    @client.event
    async def on_raw_reaction_remove(payload):
        await handle_reaction_role(payload, add=False)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        messages_to_delete = ['/', 'fuck', 'suka']
        if any(word in message.content.lower() for word in messages_to_delete):
            await message.delete()

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message=message, user_message=user_message, is_private=True)
        else:
            await send_message(message=message, user_message=user_message, is_private=False)

    client.run(TOKEN)
