import requests
import json

# Define the URL and the input data
url = "https://masudfws.us-east-2.aws.modelbit.com/v1/Linear_Regression_Predict_Duration/latest"
input_data = {
    "data": [0.3, 0.2, 0.5, 1, 0.8, 0.6, 0.9]
}

# Make the POST request
response = requests.post(url, data=json.dumps(input_data))

# Print the result
print(response.json())