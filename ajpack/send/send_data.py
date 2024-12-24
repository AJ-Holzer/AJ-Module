import requests, json #type:ignore
from typing import Any

def send_file(
        file_path: str,
        webhook_url: str
) -> None:
    """
    Sends a file to a discord webhook.

    :param file_path: The path of the file to send.
    :param webhook_url: The webhook url of the target dc server.
    """
    with open(file_path, "rb") as f:
        # Create a dictionary of file objects to be sent to the webhook_url
        files = {'file': f}
        
        # Send the zip file to the Discord webhook_url
        response = requests.post(webhook_url, files=files)

        # Check the response from the web server
        if response.status_code != 200:
            raise Exception(f"Error while sending the file to discord! Status code: {response.status_code}")
        
def send_embed(
        url: str,
        embed: dict[str, Any] # title, description, color, fields
) -> None:
    """
    Sends an embed to a discord webhook.\n
    embed example:
        embed = {
            "title": "TITLE",
            "description": "DESCRIPTION",
            "color": 16711680,  # Red color
            "fields": [
                {
                    "name": "Field 1",
                    "value": "Some value",
                    "inline": False
                },
                {
                    "name": "Field 2",
                    "value": "Another value",
                    "inline": False
                }
            ]
        }

    :param url: The embed url.
    :param embed: The embed to be sent.
    """
    # Create the payload to send
    payload = {
        "embeds": [embed]
    }

    # Send the payload to the Discord webhook
    response = requests.post(url=url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

    # Check the status code of the response
    if response.status_code != 204:
        raise Exception(f"Error while sending the embed to discord! Status code: {response.status_code}")
