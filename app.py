from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK"

@app.route('/dday', methods=['POST'])
def dday():
    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": "시험까지 D-30일 남았습니다."
                }
            }]
        }
    })

if __name__ == '__main__':
    app.run()
