from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# 출제할 파이썬 문제와 정답 리스트
questions = [
    {
        "code": 'print("Hello, World!")',
        "answer": 'Hello, World!'
    },
    {
        "code": 'for i in range(3):\n    print(i)',
        "answer": '0\n1\n2'
    },
    {
        "code": 'print(2 + 3 * 4)',
        "answer": '14'
    },
    {
        "code": 'print("Python"[::-1])',
        "answer": 'nohtyP'
    },
]

@app.route("/")
def index():
    # 무작위 문제 선택
    question = random.choice(questions)
    return render_template("index.html", code=question["code"], answer=question["answer"])

@app.route("/check", methods=["POST"])
def check():
    user_answer = request.json.get("user_answer").strip()
    correct_answer = request.json.get("correct_answer").strip()
    
    if user_answer == correct_answer:
        return jsonify({"result": "🎉 정답입니다! 축하합니다!"})
    else:
        return jsonify({"result": "❌ 틀렸습니다. 다시 시도해보세요!"})

if __name__ == "__main__":
    app.run(debug=True)
