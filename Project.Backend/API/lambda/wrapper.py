from errors import *
import json

def buildHeaders():
    return{
        'Headers': 
        {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

def buildFunction(opertaion, data, count, lambdaError):
    try:
        if lambdaError:
            print("Unexpected error {lambdaError.statusCode}".format(lambdaError = lambdaError))
            return{
                'statusCode': lambdaError.statusCode,
                'headers': buildHeaders(),
                'body': json.dumps(buildBody(operation=opertaion, body=lambdaError.toLambda(), count=count)),
            }
        else:
            # If not have an lambda error
            return{
                'statusCode': 200,
                'headers': buildHeaders(),
                'body': json.dumps(buildBody(operation=opertaion, body=data, count=count)),
            }
    except:
        print('except')
    

def buildBody(operation, body, count):
        return {
        'Operation': operation,
        'Count': count,
        'Items': body
        }

# Tests
le = LambdaError("","Delete information error","")
err = deleteDataFailed(le)
#print(deleteDataFailed(le).toLambda())

print('')
print(buildFunction('GET', "My first item", 1, lambdaError=err))