```python
import csv

def csv_upload(file_path):
    userWallets = []
    with open(file_path, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            userWallets.append(lines[0])
    return userWallets

# Test the function
print(csv_upload('user_wallets.csv'))
```