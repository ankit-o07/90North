import json
import boto3
import base64
import os


s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        
        bucket_name = os.environ['BUCKET_NAME']
        
        
        file_content = event['body']  
        file_name = event['headers']['filename']  
        file_type = event['headers']['filetype']  
        
        
        decoded_file = base64.b64decode(file_content)
        
        
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=decoded_file,
            ContentType=file_type
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File uploaded successfully!',
                'file_name': file_name
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'File upload failed!',
                'error': str(e)
            })
        }
