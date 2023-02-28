from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def get_bgp_routing_info(asn):
    url = f"https://api.bgpview.io/asn/{asn}/prefixes"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    return data

def get_prefix_visualization(prefixes):
    visualization = ""
    for prefix in prefixes:
        visualization += f"<div>{prefix['prefix']}</div>"
    return visualization

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        asn = request.form.get("asn")
        data = get_bgp_routing_info(asn)
        if 'data' in data and 'ipv4_prefixes' in data['data']:
            prefixes = data['data']['ipv4_prefixes']
            visualization = get_prefix_visualization(prefixes)
            return render_template("result.html", prefixes=visualization)
        else:
            return render_template("result.html", error="No routing information available for this ASN.")
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8084)
