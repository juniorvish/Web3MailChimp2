```python
import requests
import json

underdogAPIKey = "YOUR_UNDERDOG_API_KEY"

def underdogAPIIntegration():
    base_url = "https://api.underdog.io"
    headers = {
        "Authorization": f"Bearer {underdogAPIKey}",
        "Content-Type": "application/json"
    }

    return base_url, headers

def createCNFTList(list_name):
    url, headers = underdogAPIIntegration()
    endpoint = "/lists"
    data = {
        "name": list_name
    }

    response = requests.post(url + endpoint, headers=headers, data=json.dumps(data))
    return response.json()

def batchSendCNFTs(list_id, cnft_ids):
    url, headers = underdogAPIIntegration()
    endpoint = f"/lists/{list_id}/send"
    data = {
        "cnft_ids": cnft_ids
    }

    response = requests.post(url + endpoint, headers=headers, data=json.dumps(data))
    return response.json()

def getCNFTList(list_id):
    url, headers = underdogAPIIntegration()
    endpoint = f"/lists/{list_id}"

    response = requests.get(url + endpoint, headers=headers)
    return response.json()

def deleteCNFTList(list_id):
    url, headers = underdogAPIIntegration()
    endpoint = f"/lists/{list_id}"

    response = requests.delete(url + endpoint, headers=headers)
    return response.json()
```