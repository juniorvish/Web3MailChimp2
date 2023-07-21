```python
import requests
from underdog_protocol_api import underdogAPIKey

def dust_cNFTs(userWallets, cNFTList):
    """
    Function to dust a specific number of wallets with cNFTs.
    """
    dusting_url = "https://api.underdogprotocol.com/dust"
    headers = {
        "Authorization": f"Bearer {underdogAPIKey}",
        "Content-Type": "application/json"
    }

    for wallet in userWallets:
        for cnft in cNFTList:
            payload = {
                "walletAddress": wallet,
                "cNFT": cnft
            }
            response = requests.post(dusting_url, headers=headers, json=payload)

            if response.status_code == 200:
                print(f"Successfully dusted {cnft} to {wallet}")
            else:
                print(f"Failed to dust {cnft} to {wallet}. Error: {response.text}")

if __name__ == "__main__":
    userWallets = ["0x123...", "0x456..."]  # Replace with actual wallet addresses
    cNFTList = ["cNFT1", "cNFT2"]  # Replace with actual cNFTs
    dust_cNFTs(userWallets, cNFTList)
```