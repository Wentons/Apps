from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

IPINFO_URL = "https://ipinfo.io/{ip}/json"

@app.route('/wenton', methods=['GET'])
def ip_sorgu():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP adresi parametresi eksik"}), 400

    try:
        response = requests.get(IPINFO_URL.format(ip=ip))
        data = response.json()

        if 'error' in data:
            return jsonify({"error": data['error']['message']}), 400

        result = {
            "IP": data.get('ip'),
            "Şehir": data.get('city'),
            "Bölge": data.get('region'),
            "Ülke": data.get('country'),
            "Konum": data.get('loc'),
            "Posta Kodu": data.get('postal'),
            "Organizasyon": data.get('org'),
            "Zaman Dilimi": data.get('timezone'),
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
