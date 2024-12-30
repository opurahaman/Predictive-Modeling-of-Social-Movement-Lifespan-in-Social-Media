from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

# API endpoints
MODEL1_URL = "https://cse499projectgroup3.us-east-1.aws.modelbit.com/v1/getMovements/latest"
MODEL2_URL = "https://cse499projectgroup3.us-east-1.aws.modelbit.com/v1/getSimilarMovements/latest"
MODEL3_URL = "https://masudfws.us-east-2.aws.modelbit.com/v1/Linear_Regression_Predict_Duration/latest"

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict/model1', methods=['POST'])
def predict_model1():
    try:
        text = request.form.get('text')
        response = requests.post("https://siammasud.us-east-1.aws.modelbit.com/v1/find_closest_movements_with_duration/latest", json={"data": text})
        result = response.json()
        
        # Adjusting the result to match the expected output format
        formatted_result = [movement["movement_name"] for movement in result.get("data", [])]
        
        # Prepare a user-friendly output
        user_friendly_result = ', '.join(formatted_result)  # Join the movement names into a single string
        
        return render_template('result.html', result=user_friendly_result)
    except Exception as e:
        return render_template('result.html', error=str(e))

@app.route('/predict/model2', methods=['POST'])
def predict_model2():
    try:
        values = [float(request.form.get(f'value{i}')) for i in range(1, 8)]
        response = requests.post(MODEL2_URL, json={"data": values})
        result = response.json()
        return render_template('result.html', result=result)
    except Exception as e:
        return render_template('result.html', error=str(e))

@app.route('/predict/model3', methods=['POST'])
def predict_model3():
    try:
        values = [
            float(request.form.get('positive_sentiment')),
            float(request.form.get('negative_sentiment')),
            float(request.form.get('neutral_sentiment')),
            float(request.form.get('counter_movement')),
            float(request.form.get('cultural_relevance')),
            float(request.form.get('political_nature')),
            float(request.form.get('legality_nature'))
        ]
        response = requests.post(MODEL3_URL, json={"data": values})
        result = response.json()
        return render_template('result.html', result=result)
    except Exception as e:
        return render_template('result.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
