import json

from src import app


def apigw_event():
    """ Generates API GW Event"""
    return [
        {
            "headers": {
                "Accept-Language": "en-US,en;q=0.8",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            },
            "pathParameters": {
                "id": "id_01",
                "user_id": "user_01",
            },
            "httpMethod": "GET",
        },
        {
            "headers": {
                "Accept-Language": "en-US,en;q=0.8",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            },
            "httpMethod": "POST",
            "body": "{\"id\":\"id_02\", \"user_id\":\"user_02\", \"body\":\"message_02\"}",
        },
        {
            "headers": {
                "Accept-Language": "en-US,en;q=0.8",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            "pathParameters": {
                "id": "id_02",
                "user_id": "user_02"
            },
            "httpMethod": "DELETE",
        }
    ]


def test_lambda_handler():
    for e in apigw_event():
        res = app.lambda_handler(e, '')
        data = json.loads(res['body'])
        if e['httpMethod'] == 'GET':
            assert res['statusCode'] == '200'
            assert data['message']['id'] == 'id_01'
            assert data['message']['user_id'] == 'user_01'
            assert data['message']['body'] == 'message_01'
        elif e['httpMethod'] == 'POST':
            assert res['statusCode'] == '201'
        elif e['httpMethod'] == 'DELETE':
            assert res["statusCode"] == '200'
            assert data['message']['id'] == 'id_02'
            assert data['message']['user_id'] == 'user_02'
            assert data['message']['body'] == 'message_02'
