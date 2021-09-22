import json

# Construct your Lambda Class

class lambda_handler:
    def __init__(self, event, context, conn):
        # Http parameters
        self.event = event
        self.context = context
        # Connection
        self.conn = conn
        # Response
        self.status_code = 200
        self.response = []
        self.body = {}

    def buildBody(self, operation, message, body, item_count):
        return {
        'Operation': operation,
        'Message': message,
        'Count': item_count,
        'Item': body
        }

    def buildResponse(self, statusCode, body):
        return {
            'statusCode': statusCode,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(body) 
        }  