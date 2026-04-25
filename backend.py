from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('frontend.html')

@app.route('/api/send-url', methods=['POST'])
def send_url():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Now, the URL will be sent a request, and its content will be fetched and returned as a response.
    try:
        import requests
        from urllib.parse import urljoin
        response = requests.get(url)
        content = response.text
        
        # Inject <base> tag to help resolve relative links
        if '<head>' in content:
            base_tag = f'<base href="{url}">'
            content = content.replace('<head>', f'<head>{base_tag}')
        
        return jsonify({'content': content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)
