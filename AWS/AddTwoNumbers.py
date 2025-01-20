import json

def lambda_handler(event, context):

    try:
        
        number1 = event.get('number1')
        number2 = event.get('number2')

       
        if number1 is None or number2 is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Both 'number1' and 'number2' are required."})
            }

      
        if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Both inputs must be numbers."})
            }

        
        result = number1 + number2

        
        return {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }

    except Exception as e:
        
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
