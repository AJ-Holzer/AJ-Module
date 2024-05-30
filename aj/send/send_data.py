import requests

def send_data(
    zip_path: str,
    webhook: str
):

    with open(zip_path, "rb") as f:
        # Create a dictionary of file objects to be sent to the webhook
        files = {'file': f}
        
        # Send the zip file to the Discord webhook
        response = requests.post(webhook, files=files)

        # Check the response from the web server
        if response.status_code != 200:
            raise Exception(f"Error while sending the file to discord! Status code: {response.status_code}")