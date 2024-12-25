import boto3
import json

# Initialize the Bedrock client
client = boto3.client('bedrock-runtime', region_name='your-region')  # Replace with your AWS region

def lambda_handler(event, context):
    try:
        # Extract the user prompt from the request
        body = json.loads(event['body'])
        user_prompt = body.get('prompt', '')

        if not user_prompt:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Prompt is required'})
            }
        
        # Construct the request body for the AI model
        request_body = {
            "modelId": "your-model-id",  # Replace with your chosen model
            "inputText": user_prompt,
            "parameters": {
                "maxTokens": 300,
                "temperature": 0.7
            }
        }

        # Invoke the Bedrock model
        response = client.invoke_model(
            modelId=request_body["modelId"],
            inputText=user_prompt,
            parameters=request_body["parameters"]
        )

        # Process the model's response
        bedrock_response = response.get('generatedText', 'No response generated')

        return {
            'statusCode': 200,
            'body': json.dumps({'response': bedrock_response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


import boto3
import json

client =  boto3.client('bedrock-runtime',region_name='us-east-1')

def lambda_handler(event, context):
    try:    
        body = json.loads(event['body'])
        user_prompt= body.get('prompt', '')

        if not user_prompt:
            return {
                'statusCode' : 400,
                'body' : json.dumps({'error': 'Prompt is required'})
            }

        request_body = {
            "modelId" : "your-model-id",
            "inputText" : user_prompt,
            "parameters" : {
                "maxTokens" : 300,
                "temperature" : 0.7
            }
        }

        response = client.invoke_model(
            modelId = request_body["modelId"],
            inputText = user_prompt,
            parameters = request_body["parameters"]
            )

        bedrock_response = response.get("generatedText","No response generated")

        return {
        'statusCode' : 200,
        'body' : json.dumps({'response' : bedrock_response})
        }
    except Exception as e:
        return {
        'statusCode' : 500,
        'body' : json.dumps({'error' : str(e)})
        }
