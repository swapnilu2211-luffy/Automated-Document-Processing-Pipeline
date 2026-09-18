import json
import boto3
from flask import Flask, jsonify

app = Flask(__name__)
# Initialize boto3 client. It will automatically use the IAM role attached to EC2!
lambda_client = boto3.client('lambda', region_name='ap-south-1')

@app.route('/')
def home():
    return "DevOps Document Processor is Running!"

@app.route('/process')
def process_doc():
    payload = {"text": "DevOps is amazing!"}
    
    # Trigger the Lambda function
    response = lambda_client.invoke(
        FunctionName='DocumentProcessor',
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
    )
    
    # Read and return the Lambda response
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))
    return jsonify(json.loads(response_payload['body']))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
