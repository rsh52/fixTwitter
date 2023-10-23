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

    if p_message == 'help':
        return '`This is a simple bot, please be kind to it. You can interact with it by using "??", but primarily all it does is change twitter.com and x.com to fixup.com.`'
       
    if "twitter.com" in p_message:
        return p_message.replace("twitter.com", "fixupx.com")
    if "x.com" in p_message:
        return p_message.replace("x.com", "fixupx.com")

    return 'I don\'t know what you said.'
