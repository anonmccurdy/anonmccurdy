from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/send-url', methods=['POST'])
def send_url():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Now, the URL will be sent a request, and its content will be fetched and returned as a response.
    try:
        import requests
        response = requests.get(url)
        return jsonify({'content': response.text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
