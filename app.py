from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Study Planner Bot Server Running!"

@app.route("/dday", methods=["POST"])
def dday():
    try:
        body = request.get_json()

        # 오픈빌더에서 전달받은 값
        exam_date = body["action"]["params"]["exam_date"]

        today = datetime.today().date()
        exam = datetime.strptime(exam_date, "%Y-%m-%d").date()

        days = (exam - today).days

        text = f"시험까지 D-{days}일 남았습니다."

    except Exception:
        text = "날짜를 YYYY-MM-DD 형식으로 입력해주세요."

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
