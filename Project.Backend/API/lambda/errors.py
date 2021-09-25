import json

class LambdaError():
    def __init__(self, statuscode, message, type):
        self.statusCode = statuscode
        self.message = message
        self.type = type

    def toLambda(self):
        return {
            'statusCode': self.statusCode,
            'body': {
                'message': self.message,
                'type': self.type
            }
        }

   
def internalError(err):
    error = LambdaError(500, err.message, 'internalError')
    return error

def notFound(obj):
    error = LambdaError(404, 'The object {obj} is not found'.format(obj=obj), 'notFound')
    return error

def putDataFailed(err):
    error = LambdaError(500, err.message, 'putFailed')
    return error

def deleteDataFailed(err):
    error = LambdaError(500, err.message, 'deleteFailed')
    return error
