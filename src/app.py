import json

from presenter.common_presenter import (MethodNotAllowedPresenter,
                                        RequestSucceededPresenter)


def create(data):
    pass


def get(data):
    return RequestSucceededPresenter.response('OK')


def update(data):
    pass


def delete(data):
    pass


def lambda_handler(event, context):
    operations = {
        'POST': lambda data: create(data),
        'GET': lambda data: get(data),
        'PUT': lambda data: update(data),
        'DELETE': lambda data: delete(data),
    }
    operation = event['httpMethod']
    payload = {}
    if operation in operations:
        if operation == 'POST':
            payload = json.loads(event['body'])
        elif operation == 'GET':
            pass
        elif operation == 'PUT':
            payload = event['pathParameters']
            payload.update(json.loads(event['body']))
        elif operation == 'DELETE':
            payload = event['pathParameters']
            payload.update(json.loads(event['body']))
        return operations[operation](payload)
    else:
        return MethodNotAllowedPresenter.response('Unsupported method {}'.format(operation))
