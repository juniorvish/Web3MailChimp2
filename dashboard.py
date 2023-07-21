```python
from flask import Flask, render_template
from underdog_protocol_api import UnderdogAPI
from action_measurement import ActionMeasurement

app = Flask(__name__)

@app.route('/dashboard')
def mvp_dashboard_display():
    underdog_api = UnderdogAPI()
    action_measurement = ActionMeasurement()

    # Get the total number of NFTs
    total_nfts = underdog_api.get_total_nfts()

    # Get the open/click rate
    open_click_rate = action_measurement.get_open_click_rate()

    return render_template('dashboard.html', total_nfts=total_nfts, open_click_rate=open_click_rate)

if __name__ == '__main__':
    app.run(debug=True)
```