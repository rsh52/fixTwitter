# fixTwitter Bot

This is a Discord bot that detects X or Twitter links and converts them to fixupx links. It is written in Python and requires a `BOT_TOKEN` equal to the Discord Bot API token.

At the moment this is not hosted on any server, for users who would like to make use of it you will need the `BOT_TOKEN` and to run `main.py` on a machine of your choosing.

You can clone this repo using:

```bash
gh repo clone rsh52/fixTwitter
```

## Usage

The `fixTwitter` bot responds to prompts starting with `??`. Once prompted, the bot will respond with a link to the fixupx version of the Twitter/X link if it detects "x.com" or "twitter.com" in the message. This will delete the original users message, but provide a new link from the `fixTwitter` bot along with a message indicating who requested the fixupx link.

![Example Usage](img/example.gif)
