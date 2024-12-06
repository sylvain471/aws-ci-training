import json

def lambda_handler(event,context):
    print("Recieved event:"+json.dumps(event,indent=2))
    message="Hello from lambda!"
    return {
        "statusCode":200,
        "body":json.dumps({
            "message":message
        })
    }
