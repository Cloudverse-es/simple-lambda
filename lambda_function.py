import awsgi
from api import create_app

#from __future__ import annotations

#from typing import List


app = create_app()


def lambda_handler(event, context):
    # TODO implement
    event['httpMethod'] = event['requestContext']['http']['method']
    event['path'] = event['requestContext']['http']['path']
    event['queryStringParameters'] = event.get('queryStringParameters', {})
    
    return awsgi.response(app, event, context)
    #return {
    #    'statusCode': 200,
    #    'body': json.dumps('Hello from Lambda!')
    #}
