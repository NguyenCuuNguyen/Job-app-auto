from flask import Flask, request, jsonify
app = Flask(__name__) #Value of __name is "server"

@app.route('/predict', methods=['POST'])


def predict():
    data = request.json
    # Process data, use your ML model, etc.
    result = your_ml_function(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
