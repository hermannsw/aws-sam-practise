class RequestSucceededPresenter:
    @staticmethod
    def response(message):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'statusCode': '200',
            'body': "{\"message\":\"" + message + "\"}",
        }


class CreateSucceededPresenter:
    @staticmethod
    def response(message):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'statusCode': '201',
            'body': "{\"message\":\"" + message + "\"}",
        }


class BadRequestPresenter:
    @staticmethod
    def response(message):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'statusCode': '400',
            'body': "{\"message\":\"" + message + "\"}",
        }


class NotFoundPresenter:
    @staticmethod
    def response(message):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'statusCode': '404',
            'body': "{\"message\":\"" + message + "\"}",
        }


class MethodNotAllowedPresenter:
    @staticmethod
    def response(message):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'statusCode': '405',
            'body': "{\"message\":\"" + message + "\"}",
        }
