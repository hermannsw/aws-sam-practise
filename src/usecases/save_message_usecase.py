class SaveMessageUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, data):
        res = self.repository.save(data)
        return res
