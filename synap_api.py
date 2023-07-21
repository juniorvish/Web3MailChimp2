```python
import requests
import json

synapAPIKey = "your_synap_api_key_here"

def synapAPIIntegration():
    url = "https://api.synap.io/v1/cNFTs"
    headers = {
        "Authorization": f"Bearer {synapAPIKey}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        cNFTList = json.loads(response.text)
        return cNFTList
    else:
        print(f"Failed to get cNFTs. Status code: {response.status_code}")
        return None

def getCnft(cnft_id):
    url = f"https://api.synap.io/v1/cNFTs/{cnft_id}"
    headers = {
        "Authorization": f"Bearer {synapAPIKey}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        cNFT = json.loads(response.text)
        return cNFT
    else:
        print(f"Failed to get cNFT. Status code: {response.status_code}")
        return None
```