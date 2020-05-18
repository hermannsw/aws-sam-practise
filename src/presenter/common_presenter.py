class RequestSucceededPresenter:
    @staticmethod
    def response(message):
        m = message.to_dict()
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'statusCode': '200',
            'body': "{\"message\":{\"id\":\"" + m['id'] + "\",\"user_id\":\"" + m['user_id'] + "\",\"body\":\""
                    + m['body'] + "\"}}",
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
