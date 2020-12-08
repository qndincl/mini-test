from flask import Flask, request, Response, render_template, jsonify
import requests
import time
import random

app = Flask(__name__, static_url_path='/static')

models = {
    "gpt2-large": "http://main-gpt2-large-jeong-hyun-su.endpoint.ainize.ai/gpt2-large/long",
    "gpt2-cover-letter": "http://main-gpt2-cover-letter-jeong-hyun-su.endpoint.ainize.ai/gpt2-cover-letter/long",
    "gpt2-reddit": "http://master-gpt2-reddit-woomurf.endpoint.ainize.ai/gpt2-reddit/long",
    "gpt2-story": "http://main-gpt2-story-gmlee329.endpoint.ainize.ai/gpt2-story/long",
    "gpt2-ads": "http://main-gpt2-ads-psi1104.endpoint.ainize.ai/gpt2-ads/long",
    "gpt2-business": "http://main-gpt2-business-leesangha.endpoint.ainize.ai/gpt2-business/long",
    "gpt2-film": "http://main-gpt2-film-gmlee329.endpoint.ainize.ai/gpt2-film/long",
    "gpt2-trump": "http://main-gpt2-trump-gmlee329.endpoint.ainize.ai/gpt2-trump/long",
    "gpt2-debate": "https://main-gpt2-debate-gmlee329.endpoint.ainize.ai/gpt2-debate/long"
}

@app.route("/gpt2", methods=["POST"])
def gpt2():
    context = request.form['context']
    model = request.form['model']
    length = request.form['length']

    url = models[model]

    if length == "short":
        # length = random.randrange(2,6)
        length = 20
    else:
        length = 20
    
    data = {
        "text": context,
        "num_samples": 5,
        "length": length
    }
    print('data : ', data)
    response = requests.post(url, data=data)
    # print('** response : ', response)
    res = response.json()
    print('**** res : ',res)
    return res


@app.route("/")
def main():
    print("fuck1")
    return render_template("index.html")


# Health Check
@app.route("/healthz", methods=["GET"])
def healthCheck():
    print("fuck2")
    return "", 200


if __name__ == "__main__":
    from waitress import serve
    print("fuck")
    serve(app, host='0.0.0.0', port=80)   