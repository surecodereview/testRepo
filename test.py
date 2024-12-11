from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/review', methods=['POST'])
def code_review():
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')
    stream = data.get('stream', False)

    if not model or not prompt:
        return jsonify({'error': 'Missing required parameters'}), 400

    # 실제 코드 리뷰 로직 대신 간단한 응답 생성
    review_response = f"Received review request for model: {model}\nPrompt: {prompt}"

    return jsonify({'response': review_response})

if __name__ == '__main__':
    app.run(debug=True)
