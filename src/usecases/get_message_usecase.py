class GetMessageUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, data):
        res = self.repository.get(data['id'], data['user_id'])
        return res
