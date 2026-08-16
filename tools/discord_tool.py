import os

import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


@tool(parse_docstring=True)
def send_discord_message(content: str) -> str:
    """Send a text message to the Discord server via webhook.

    Args:
        content: The text to post to Discord. Must be under 2000 characters
            (Discord's hard limit) — keep it concise. If the information
            came from a web search, include the source URLs (e.g. under a
            "Sources:" heading) so readers can verify the information.
    """
    if not DISCORD_WEBHOOK_URL:
        raise RuntimeError("DISCORD_WEBHOOK_URL is not set in the environment")

    response = requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
    if not response.ok:
        raise RuntimeError(
            f"Discord webhook returned {response.status_code}: {response.text}"
        )
    return "Message sent to Discord successfully."
