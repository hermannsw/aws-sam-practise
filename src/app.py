import json

from model.message_model import MessageModel
from presenter.common_presenter import (BadRequestPresenter,
                                        CreateSucceededPresenter,
                                        MethodNotAllowedPresenter,
                                        RequestSucceededPresenter)
from repository.message_repository import Repository
from usecases.delete_message_usecase import DeleteMessageUseCase
from usecases.get_message_usecase import GetMessageUseCase
from usecases.save_message_usecase import SaveMessageUseCase


def create(data):
    repository = Repository(MessageModel)
    usecase = SaveMessageUseCase(repository)
    res = usecase.execute(data)
    if isinstance(res, ValueError):
        return BadRequestPresenter.response('Message not created.')
    return CreateSucceededPresenter.response('Message Created.')


def get(data):
    repository = Repository(MessageModel)
    usecase = GetMessageUseCase(repository)
    res = usecase.execute(data)
    return RequestSucceededPresenter.response(res)


def update(data):
    pass


def delete(data):
    repository = Repository(MessageModel)
    usecase = DeleteMessageUseCase(repository)
    res = usecase.execute(data)
    return RequestSucceededPresenter.response(res)


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
            payload = event['pathParameters']
        elif operation == 'PUT':
            payload = event['pathParameters']
            payload.update(json.loads(event['body']))
        elif operation == 'DELETE':
            payload = event['pathParameters']
        return operations[operation](payload)
    else:
        return MethodNotAllowedPresenter.response('Unsupported method {}'.format(operation))
