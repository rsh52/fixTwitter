import random

def get_response(message: str) -> str:
    """
    Given a message, returns a response based on the content of the message.

    Args:
        message (str): The message to be processed.

    Returns:
        str: The response to the message.
    """
    p_message = message.lower()

    if p_message == 'hello':
        return 'Howdy!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    help_message = (
    "> fixTwitter is a simple Discord bot that fixes twitter.com and x.com links to fixup.com. \
To use it, simply type `??` followed by your message. If your message contains a twitter.com \
or x.com link, it will be replaced with a fixup.com link. \
For example, `??https://twitter.com` will be replaced with `https://fixup.com`. \
The bot will remove the original post, but replace it with a message of it's own and credit to the OP's username.\
    \n> fixTwitter will also respond to: \n> - `??hello`: A greeting \n> - `??ping`: Check fixTwitter's latency or response time to the server \
    \n> - `??roll`: A random number between 1 and 6"
    )

    if p_message == 'help':
        return help_message

    return r'Sorry, I don\'t know what you said. ¯\_(ツ)_/¯ I\'m just a little bird bot, try `??help` to see what I can do!'
