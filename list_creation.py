```python
import requests
from underdog_protocol_api import underdogAPIKey

def cNFTListCreation(cNFTList):
    url = "https://api.underdogprotocol.com/createList"
    headers = {
        "Authorization": underdogAPIKey,
        "Content-Type": "application/json"
    }
    data = {
        "cNFTList": cNFTList
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("List created successfully.")
    else:
        print("Failed to create list. Error: ", response.text)

if __name__ == "__main__":
    cNFTList = ["cNFT1", "cNFT2", "cNFT3"]
    cNFTListCreation(cNFTList)
```