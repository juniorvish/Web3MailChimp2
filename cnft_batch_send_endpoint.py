```python
from flask import Flask, request, jsonify
from underdog_protocol_api import UnderdogAPI

app = Flask(__name__)
underdog_api = UnderdogAPI()

@app.route('/send_cnft_batch', methods=['POST'])
def send_cnft_batch():
    data = request.get_json()
    user_wallets = data.get('userWallets')
    cnft_list = data.get('cNFTList')

    if not user_wallets or not cnft_list:
        return jsonify({'message': 'Missing required data'}), 400

    try:
        for wallet in user_wallets:
            for cnft in cnft_list:
                underdog_api.send_cnft(wallet, cnft)
        return jsonify({'message': 'Batch send successful'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```