import responses
import discord
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def send_message(message, user_message, is_private):
    """
    Sends a message to a user or channel based on the user's message and whether it's private or not.

    Args:
        message (discord.Message): The message object that triggered the bot.
        user_message (str): The message sent by the user.
        is_private (bool): Whether the message should be sent privately to the user or in the channel.

    Raises:
        discord.errors.HTTPException: If there was an error sending the message.

    Returns:
        None
    """
    try:
        response = responses.get_response(user_message)
        send_func = message.author.send if is_private else message.channel.send
        await send_func(response)
    except discord.errors.HTTPException as e:
        print(e)


def run_discord_bot():
    """
    Runs a Discord bot that listens for messages and responds to them.

    The bot connects to Discord using the provided TOKEN and listens for messages
    in all channels it has access to. If a message starts with a question mark (?),
    the bot will respond to the message in a private message to the user who sent it.
    Otherwise, the bot will respond to the message in the same channel it was sent in.

    Args:
        None

    Returns:
        None
    """
    TOKEN = BOT_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message.startswith("??"):
            user_message = user_message[2:]
            if "x.com" in user_message:
                new_content = user_message.replace("x.com", "fixupx.com")
                await message.delete()  # Delete the user's message
                await message.channel.send(f"fixTwitter post by `{username}`")
                await message.channel.send(
                    new_content
                )  # Send a new message with updated content
            elif "twitter.com" in user_message:
                new_content = user_message.replace("twitter.com", "fixupx.com")
                await message.delete()  # Delete the user's message
                await message.channel.send(f"fixTwitter post by `{username}`")
                await message.channel.send(
                    new_content
                )  # Send a new message with updated content
            else:
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
