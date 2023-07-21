```python
import requests
import json

# Dispatch API Key
dispatchAPIKey = "your_dispatch_api_key"

# Base URL for Dispatch API
base_url = "https://api.dispatch.com"

# Headers for API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {dispatchAPIKey}"
}

def send_message(userWallets, cNFTNotification):
    """
    Function to send messages to users via Dispatch API
    """
    # Endpoint for sending messages
    url = f"{base_url}/send_message"

    # Message data
    data = {
        "wallet_addresses": userWallets,
        "message": cNFTNotification
    }

    # Send POST request to Dispatch API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if request was successful
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def get_messages():
    """
    Function to get messages from Dispatch API
    """
    # Endpoint for getting messages
    url = f"{base_url}/get_messages"

    # Send GET request to Dispatch API
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Parse response JSON
        messages = response.json()

        # Print messages
        for message in messages:
            print(f"Message ID: {message['id']}")
            print(f"Message: {message['message']}")
            print(f"Wallet Address: {message['wallet_address']}")
            print("\n")
    else:
        print(f"Failed to get messages. Status code: {response.status_code}")
```