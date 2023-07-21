```python
import requests
from underdog_protocol_api import underdogAPIIntegration
from synap_api import synapAPIIntegration

class CNFTInterface:
    def __init__(self, underdogAPIKey, synapAPIKey):
        self.underdogAPIKey = underdogAPIKey
        self.synapAPIKey = synapAPIKey
        self.cNFTList = []

    def getCNFTList(self):
        self.cNFTList = synapAPIIntegration(self.synapAPIKey)
        return self.cNFTList

    def viewCNFT(self, cNFTId):
        for cNFT in self.cNFTList:
            if cNFT['id'] == cNFTId:
                return cNFT
        return None

    def notifyCNFT(self, cNFTId):
        cNFT = self.viewCNFT(cNFTId)
        if cNFT:
            # Send notification to user about the cNFT
            # This is a placeholder for the actual notification code
            print(f"Notification sent for cNFT: {cNFT['name']}")
        else:
            print("cNFT not found")

if __name__ == "__main__":
    cnft_interface = CNFTInterface('underdogAPIKey', 'synapAPIKey')
    cnft_interface.getCNFTList()
    cnft_interface.viewCNFT('cNFTId')
    cnft_interface.notifyCNFT('cNFTId')
```