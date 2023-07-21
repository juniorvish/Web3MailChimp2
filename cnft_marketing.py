```python
import requests
from underdog_protocol_api import underdogAPIIntegration
from dispatch_api import dispatchAPIIntegration
from utm_parameters import generateUTMParameters

def cNFTMarketingCampaign(cNFTList, userWallets, underdogAPIKey, dispatchAPIKey):
    # Generate UTM parameters for tracking
    utmParameters = generateUTMParameters("cNFT Marketing Campaign")

    # Loop through each cNFT in the list
    for cNFT in cNFTList:
        # Create a new list in Underdog for the cNFT
        list_id = underdogAPIIntegration.createList(underdogAPIKey, cNFT)

        # Add all user wallets to the list
        for wallet in userWallets:
            underdogAPIIntegration.addWalletToList(underdogAPIKey, list_id, wallet)

        # Create a new message in Dispatch for the cNFT
        message_id = dispatchAPIIntegration.createMessage(dispatchAPIKey, cNFT, utmParameters)

        # Send the message to all wallets in the list
        dispatchAPIIntegration.sendMessageToList(dispatchAPIKey, message_id, list_id)

    print("cNFT Marketing Campaign has been successfully executed.")
```