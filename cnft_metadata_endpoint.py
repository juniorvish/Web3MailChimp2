```python
from flask import Flask, request, jsonify
from underdog_protocol_api import UnderdogAPI

app = Flask(__name__)
underdog_api = UnderdogAPI()

@app.route('/update_metadata', methods=['POST'])
def update_metadata():
    data = request.get_json()
    cNFTMetadata = data.get('cNFTMetadata', {})
    response = underdog_api.update_metadata(cNFTMetadata)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```