from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        asn = request.form['asn']
        current_info = get_bgp_routing_info(asn)
        return render_template('index.html', asn=asn, routing_info=current_info)
    return render_template('index.html')

def get_bgp_routing_info(asn):
    url = f'https://api.bgpview.io/asn/{asn}/prefixes'
    response = requests.get(url)
    data = response.json()
    prefixes = data['data']['ipv4_prefixes']
    return prefixes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)

