```python
import requests
from underdog_protocol_api import underdogAPIKey

def cNFTMessageDrafting(cNFTList, message):
    """
    Function to draft cNFT messages using the Underdog Protocol API.
    """
    url = "https://api.underdogprotocol.com/draftMessage"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {underdogAPIKey}"
    }

    data = {
        "cNFTList": cNFTList,
        "message": message
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Message drafted successfully.")
    else:
        print(f"Failed to draft message. Status code: {response.status_code}")

if __name__ == "__main__":
    cNFTList = ["cNFT1", "cNFT2", "cNFT3"]
    message = "This is a test message for cNFTs."
    cNFTMessageDrafting(cNFTList, message)
```