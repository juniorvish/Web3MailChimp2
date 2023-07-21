```python
import pandas as pd
from underdog_protocol_api import UnderdogAPI
from action_measurement import ActionMeasurement

class MailchimpScore:
    def __init__(self, underdogAPIKey):
        self.underdogAPI = UnderdogAPI(underdogAPIKey)
        self.actionMeasurement = ActionMeasurement()

    def calculate_score(self, userWallets):
        userEngagementScore = {}
        for wallet in userWallets:
            userActions = self.actionMeasurement.get_user_actions(wallet)
            userEngagementScore[wallet] = self._score_formula(userActions)
        return userEngagementScore

    def _score_formula(self, userActions):
        # Define the weights for each action
        weights = {
            'open': 1,
            'click': 2,
            'conversion': 3
        }

        score = 0
        for action, count in userActions.items():
            score += weights[action] * count
        return score

    def update_user_engagement(self, userEngagementScore):
        for wallet, score in userEngagementScore.items():
            self.underdogAPI.update_user_engagement(wallet, score)

if __name__ == "__main__":
    underdogAPIKey = "your_underdog_api_key"
    mailchimpScore = MailchimpScore(underdogAPIKey)

    # Load user wallets from a CSV file
    userWallets = pd.read_csv('user_wallets.csv')['wallet'].tolist()

    # Calculate the engagement score for each user
    userEngagementScore = mailchimpScore.calculate_score(userWallets)

    # Update the engagement score in the Underdog API
    mailchimpScore.update_user_engagement(userEngagementScore)
```