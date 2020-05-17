from pynamodb.exceptions import DoesNotExist


class DeleteMessageUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, data):
        message = self.repository.get(data['id'], data['user_id'])
        if isinstance(message, DoesNotExist):
            return DoesNotExist()

        res = self.repository.delete(message)
        return res
