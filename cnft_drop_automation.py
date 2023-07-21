```python
import schedule
import time
from underdog_protocol_api import underdogAPIIntegration
from csv_upload import csvUpload

# Define the function to automate cNFT drops
def cNFTDropAutomation(dropSchedule, underdogAPIKey, csvFilePath):
    # Import user wallets via CSV during drops
    userWallets = csvUpload(csvFilePath)

    # Create a cNFT project in Underdog
    underdogAPIIntegration(underdogAPIKey, userWallets)

    print("cNFT drop has been automated.")

# Define the schedule for cNFT drops
dropSchedule = "every 1 week"

# Define the Underdog API key
underdogAPIKey = "your_underdog_api_key"

# Define the CSV file path for user wallets
csvFilePath = "user_wallets.csv"

# Schedule the cNFT drop automation
schedule.every(1).weeks.do(cNFTDropAutomation, dropSchedule, underdogAPIKey, csvFilePath)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
```