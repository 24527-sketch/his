from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Study Planner Bot Server Running!"
    })

@app.route("/skill", methods=["POST"])
def skill():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "공부 플래너 챗봇입니다."
                    }
                }
            ]
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
