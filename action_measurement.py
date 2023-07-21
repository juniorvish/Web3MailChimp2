```python
import requests
from underdog_protocol_api import underdogAPIKey
from dispatch_api import dispatchAPIKey
from synap_api import synapAPIKey

cNFTActionData = {}

def cNFTActionMeasurement(action_type, user_wallet, cNFT_id):
    """
    Function to measure open, conversion, and other actions using cNFTs as on-chain stamps or via the site.
    """
    global cNFTActionData

    # Define the endpoint URL
    url = "https://api.underdogprotocol.com/measure_action"

    # Define the headers for the API request
    headers = {
        "Underdog-API-Key": underdogAPIKey,
        "Dispatch-API-Key": dispatchAPIKey,
        "Synap-API-Key": synapAPIKey,
        "Content-Type": "application/json"
    }

    # Define the data for the API request
    data = {
        "action_type": action_type,
        "user_wallet": user_wallet,
        "cNFT_id": cNFT_id
    }

    # Send the API request and get the response
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Update the cNFT action data
        cNFTActionData = response.json()
        return cNFTActionData
    else:
        return None
```